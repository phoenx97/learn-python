from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit return to continue, CTRL-C to abort."
raw_input()

outdata = open(to_file, 'w').write(indata)
print "Alright, all done."
