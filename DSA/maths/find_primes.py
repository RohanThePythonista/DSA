input_list = [i for i in range(2, 51)]
print(input_list)

# naive approach
for item in input_list:
    count = 0
    for i, val in enumerate(input_list):
        if item % val == 0:
            count += 1
    if count > 1:
        print("{} is not prime number".format(item))
    else:
        print("{} is prime number".format(item))

