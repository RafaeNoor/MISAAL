
import sys

benchmark_name = sys.argv[1]

generated_halide_name = "{}/bin/{}.halide_generated.cpp".format(benchmark_name, benchmark_name)

with open(generated_halide_name, "r") as InputFile:
    input_lines = InputFile.readlines()

with open("pim_fused_lowering.h", "r") as KernelFile:
    kernel_lines = KernelFile.readlines()


def is_misaal_decl(line):
    tokens = line.split()
    if len(tokens) < 2:
        return False
    return tokens[1].startswith("misaal_node")

previous_line_misaal_decl = False
output_lines = []

for idx, line in enumerate(input_lines):
    if idx == 0:
        output_lines.append(line)
        continue

    if is_misaal_decl(input_lines[idx - 1]) and not is_misaal_decl(input_lines[idx]):
        output_lines += kernel_lines

    output_lines.append(line)




with open(generated_halide_name, "w") as OutputFile:
    OutputFile.write(" ".join(output_lines))


