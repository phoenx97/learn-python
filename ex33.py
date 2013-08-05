def append_to_list(numbers, max_num, increment):
    i = 0
    while i < max_num:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# study drill - doing the same thing with a for loop
#    for num in range(0, max_num, increment):
#        print "At the top i is %d" % num
#        numbers.append(num)

#        print "Numbers now: ", numbers
#        print "At the bottom i is %d" % num


max_num = 6
increment = 1
numbers = []

append_to_list(numbers, max_num, increment)

print "The numbers: "

for num in numbers:
    print num
