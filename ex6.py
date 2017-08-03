#sets variable
types_of_people = 10

#sets x to a string with types_of_people displayed as well
x = f"There are {types_of_people} types of people"

#sets binary & do_not variables
binary = "bianary"
do_not = "don't"

#sets y to string, which includes variable binary and do_not
y = f"Those who know {binary} and those who {do_not}."

#prints x & y
print(x)
print(y)

#prints I said + variable x as a string
print(f"I said: {x}")

# prints I also said + y as a variable
print(f"I also said: '{y}'")

#creates hilarious variable and sets it to False
hilarious = False

#sets joke_evaluation to string an open parameter for a variable
joke_evaluation = "Isn't that joke so funny?! {}"

#prints joke_evaluation, uses format function, parameter is variable: hilarious
print(joke_evaluation.format(hilarious))

#w + e to strings
w = "This is the left side of..."
e = "a string with a right side."

#prints w + e
print(w + e)
