import itertools
names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
countries = ['Australia', 'Spain', 'Global', 'Argentina', 'USA', 'Mexico']
for count, names, countries in zip(itertools.count(), names, countries):
    print(f"{count}.", names, countries)
