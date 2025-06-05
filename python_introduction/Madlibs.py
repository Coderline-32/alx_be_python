outer_count= 1
while outer_count <=5:
    inner_count = 1
    while inner_count<= outer_count:
        print("*", end= "")
        inner_count += 1
    print()
    outer_count += 1