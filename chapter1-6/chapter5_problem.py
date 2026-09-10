words = {
    "Pani" : "Water",
    "Boi" : "Book",
    "Bari" : "House",
    "Kolom" : "Pen"
}
# word = input("Enter a your word: ")
# print(words[word])


# interview question
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s) # it will print 20 and 20.0 because they are same but 20 is int and 20.0 is float so it will print only one of them
print(len(s)) # it will print 2 because there are only 2 unique elements in the set


# problem 6
d = {}

name = input("Enter your friend's name: ")
language = input("Enter your favourite language: ")
d.update({name: language})

name = input("Enter your friend's name: ")
language = input("Enter your favourite language: ")
d.update({name: language})

name = input("Enter your friend's name: ")
language = input("Enter your favourite language: ")
d.update({name: language})

name = input("Enter your friend's name: ")
language = input("Enter your favourite language: ")
d.update({name: language})

print(d)