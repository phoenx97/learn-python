# comma at the end of print prevents ending with a newline
print "How old are you?",
age = raw_input()  # read line from input, converting it into a string
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy (Rep)." % (
    age, height, weight)

print "So, you're %s old, %s tall and %s heavy (String)." % (
    age, height, weight)
