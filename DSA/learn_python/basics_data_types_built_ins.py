my_list = range(20)

output = list(map(lambda x: x % 2, my_list))
print(output)
output = list(filter(lambda x: x % 2, my_list))
print(output)
output = list((lambda x: x % 2, my_list))

# print(output.__next__())
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
print(noprimes)
primes = [x for x in range(2, 50) if x not in noprimes]
print (primes)