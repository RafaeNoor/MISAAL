import ast
import json






def histogram_results(fpath, fold_halide = True):
    results = {}
    with open(fpath, "r") as File:
        data = json.load(File)

        for key in data:
            results[key] = {}
            keys = data[key]

            for entry in keys:
                tokens = ast.literal_eval(entry)

                for tk in tokens:
                    if fold_halide and tk.startswith("typed:unsigned"):
                        continue
                    if tk not in results[key]:
                        results[key][tk] = 0
                    results[key][tk]+= 1


        with open("histogram_summary.json", "w+") as ResultFile:
            ResultFile.write(json.dumps(results, indent = 4))


    return results



def histogram_summary(results):

    for key, dict_ in results.items():
        print("="*10, key , "="*10,)
        tokens = [tk for tk in dict_]
        sorted_tokens = sorted(tokens, key = lambda x: dict_[x])

        for idx, tk in enumerate(sorted_tokens):
            print("[",idx+1,"]\t",tk,":", dict_[tk])


        print(sorted_tokens)




