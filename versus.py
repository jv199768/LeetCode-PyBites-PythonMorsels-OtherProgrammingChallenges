
# f-string vs str.format() vs. concatenation

name = 'Jaivir'
subject = 'Python'
print(f"My name is {name}. Let's learn {subject}.")

name = 'Jaivir'
subject = 'Python'
print("My name is {}. Let's learn {}.".format(name, subject))

name = 'Jaivir'
subject = 'Python'
print("My name is" + name + ". Let's learn" + subject + ".")


