# single line string
course1 = "Python Programming"
course2 = 'Python Programming'

# multi-line string
course3 = """
Hello
Python Programming
"""
course4 = '''
Hello
Python Programming
'''

# string functions
print(len(course1))

print(course1[0])
print(course1[-1])

# slice/substring
print(course1[0:3])  # excluding the char at end index
print(course1[0:])
print(course1[:3])
print(course1[:])

# escape sequences
course5 = "Python \"Programming"
course6 = 'Python \'Programming'
course7 = 'Python \\Programming'
course8 = 'Python \nProgramming'
print(course8)


# Format strings
first = "Sivaram"
last = "Koduri"
full_name = first + " " + last

formatted_full_name = f"{len(first)} {last} {2 + 2}"
print(formatted_full_name)


# string methods
course9 = ' Python Programming '
print(course9.upper())  # returns a new string
print(course9)
print(course9.lower())
print(course9.title())

print(course9.strip())
print(course9.lstrip())
print(course9.rstrip())

print(course9.find("p"))  # case sensitive strings
# returns lowest index at which the given substring found
print(course9.find("on"))
print(course9.replace("P", "J"))

print("p" in course9)  # returns Boolean value
print("p" not in course9)
