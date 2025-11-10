

text = "the following example creates an array list with a capacity of 50 elements. four elements are then added to the arraylist and the arraylist is trimmed accordingly"

words = text.split()

result = [word for word in words if word.lower().startswith(('a', 'e'))]

print(result)