# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Jessica Harris


def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()


#Exercise 3.1
# Error is repeat_lyrics is not defined.

#Exercise 3.2
# Output:
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.

#Exercise 3.3

def right_justify(s):
	spaces = 70 - len(s)
	print ' '*spaces + s

right_justify("allen")

#Exercise 3.4

def do_twice(f,val):
	f(val)
	f(val)

def print_spam():
	print 'spam'

def print_twice(spam_string):
	print spam_string
	print spam_string

def do_four(f,val):
	do_twice(f,val)
	do_twice(f,val)

do_twice(print_twice, 'spam')
do_four(print_twice, 3)

