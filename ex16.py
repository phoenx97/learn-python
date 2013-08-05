from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL+C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')  # defaults to read only, must specify 'w'

print "Truncating the file. Goodbye!"
target.truncate()  # don't actually need to truncate if opening in 'w'

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# study drill - reduce writes to one line
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()

# study drill - spit the file back out
test_write = open(filename)
print "Contents of %r:" % filename
print test_write.read()
