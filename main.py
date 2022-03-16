myfile = 'numbers.txt'
sum = 0
even = 0
odd = 0
with open(myfile) as fh:
    for line in fh:
        numbers = line.strip().split(',')
        for ns in numbers:
            sum += int(ns)
            if(int(ns) % 2 == 0):
                even += int(ns)
            else:
                odd += int(ns)
print(sum)
print(even)

print(odd)



