from  bitserial_fused_sema import bitserial_fused_sema


num_eq_class = 0
num_ctx = 0
for eq_class in bitserial_fused_sema:
    num_eq_class += 1

    for ctx in bitserial_fused_sema[eq_class]['target_instructions']:
        num_ctx += 1



print("Num Fused EqClasses:", num_eq_class)
print("Num Fused Concrete Contexts:", num_ctx)

avg = num_ctx / num_eq_class

print("Average # ctx per eq class:", avg)

