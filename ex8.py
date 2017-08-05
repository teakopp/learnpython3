#creates a string with inputs and stores it into a variable
formatter = "{} {} {} {}"

#puts 1,2,3,4 into the formatter string inputs
print(formatter.format(1, 2, 3, 4))

#puts one, two, three, four into string
print(formatter.format("one", "two", "three", "four"))

#puts boolean values into string
print(formatter.format(True, False, False, True))

#recursive values are put into variable
print(formatter.format(formatter, formatter, formatter, formatter))

#inputs strings into  variable
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
