# Author Vladimir SR
from io import open

text = "We are going to test files \nAt least that is what they say.\nBy the way, this file DOESN'T EXIST YET"
file = open("vladimir.txt", "w", encoding="utf8")
file.write(text)
file.close()

file = open("vladimir.txt", "w", encoding="utf8")
text = "THIS WRITES AND DELETES EVERYTHING"
file.write(text)
file.close()

file = open("vladimir.txt", "a", encoding="utf8")
text = "\nTHIS WRITES AND DOESN'T DELETES EVERYTHING"
file.write(text)
file.write(text)
file.close()

file = open("vladimir.txt", "r", encoding="utf8")
text = file.readlines()
file.close()
print(text)

print(text[-1])

file = open("multiline.txt", "w", encoding="utf8")
text = "Line 1\nLine 2\nLine 3"
file.write(text)
file.close()

file = open("multiline.txt", "r", encoding="utf8")
file.readline()
