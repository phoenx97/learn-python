print "Mary had a little lamb."
print "It's fleece was what as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # print . ten times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# comma at the end adds space instead of making new line
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# should do the same thing
print(end1 + end2 + end3 + end4 + end5 + end6 + ' ' +
      end7 + end8 + end9 + end10 + end11 + end12)
