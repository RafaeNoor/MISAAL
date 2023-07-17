import json
import sys
data = ""


with open("test_str.txt", "r") as ReadFile:
    data = ReadFile.read()





def identify_swizzles(bv_streams, target_vector_sizes = [], max_distinct_inputs = 2, var_to_size_map = {}, prec = 16):

    data = bv_streams.strip().split("STORE")
    iterations = []

    target_vector_sizes.sort()

    for iter in data:
        iterations.append(iter.strip().split("\n"))


    streams = {}
    for iter in iterations:
        iter_stream  = {}
        for extract in iter:
            if "EXTRACT" not in extract:
                continue

            src = extract.split("FROM")[-1].strip()

            if src not in iter_stream:
                iter_stream[src] = []

            ranges = extract.split('EXTRACT')[-1].split('FROM')[0].strip()
            iter_stream[src].append(ranges)

        for key in iter_stream:
            if key not in streams:
                streams[key] = []

            streams[key].append(iter_stream[key])




    test_key = list(streams.keys())[0]
    a_streams = streams[test_key]
    a_size = var_to_size_map[test_key]

    base_vect_size = a_size

    num_a_sources = min(len(a_streams[0]), max_distinct_inputs)
    print(a_streams[0])
    print("Num Sources: ", num_a_sources)

    input_slice_size =  a_size // num_a_sources
    num_shuffle_iterations = 1



    for target_size in target_vector_sizes:
        if target_size >= input_slice_size and target_size % input_slice_size == 0:
            num_shuffle_iterations = target_size // input_slice_size # 4
            print("Using Target Size:", target_size)

            base_vect_size = target_size

            break



    step_size = base_vect_size // (num_shuffle_iterations )# * num_a_sources)
    print("Step Size: ", step_size)

    print("Num Shuffle iterations: ", num_shuffle_iterations)

    for iteration in range(num_shuffle_iterations):

        #starts = [a_size // (num_a_sources *prec) - 1] * num_a_sources

        starts = [((step_size  // prec))-1] * num_a_sources

        print("Starts", starts)

        shuffle_vector_args = []

# Each iteration you should sort each stream of extract in descending order

        for idx, a_iter in enumerate(a_streams):

            #if len(a_iter) != num_a_sources:
            #    break

            for src_idx, rng in enumerate(a_iter):
                hi = int(rng.split(" ")[0])
                lo = int(rng.split(" ")[1])


                prec = hi - lo + 1


                index_modulo = src_idx % num_a_sources

                slice_range = (((index_modulo * base_vect_size) + (iteration * step_size)) // prec) + (starts[index_modulo] )
                shuffle_vector_args.append((index_modulo,slice_range))
                starts[index_modulo] -= 1







        #print("A Streams")
        #print(json.dumps(a_streams, indent= 4))

        print("Shuffle vector arguments")
        print(shuffle_vector_args)


identify_swizzles(data, target_vector_sizes = [2048, 1024], max_distinct_inputs =4, var_to_size_map = {"Vu": 1024, "Vv": 1024}, prec = 8)


#identify_swizzles(data, target_vector_sizes = [512, 256, 128, 64], max_distinct_inputs = 2, var_to_size_map = {"a": 512, "Vv": 512}, prec = 16)
