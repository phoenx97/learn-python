"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """"
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# \n still works in triple-quote
# triple-single-quote does the same

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# custom formatting
custom = "\t%05d | %05.1f | %s" % (11, 22, "Hello there")

print custom

print "debug representation:\n%r" % custom

#while True:
#    for i in ["/", "-", "|", "\\", "|"]:
#        print "%s\r" % i
