my_name = 'Peter Le'
my_age = 27
my_height = 5 * 12 + 8  # inches
my_weight = 150  # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# lot of formatting
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "%05d is 0 padded with 5 length." % my_age
print("%.2f is floating point represented with 2 precision "
      "decimal places" % my_weight)
print "%+d will show a sign character (+/-) before the number." % my_height
print "%-5d takes up 5 characters left adjusted." % my_age
print "% d will have a black character before the number if positive." % my_age

test_string = "%05d is 0 padded with 5 length." % my_age
print "%r is a %%r printed string." % test_string

cm_per_inch = 2.54
lbs_per_kg = 0.453592
print "Height in cm: %.2f." % (cm_per_inch * my_height)
print "Weight in kg: %.2f." % (lbs_per_kg * my_weight)
