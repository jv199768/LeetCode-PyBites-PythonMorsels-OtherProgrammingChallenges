# Example of nested walrus operators 
values = [5, 15, 25, 35, 45]
threshold = 20
results = []

for value in values:
    if (above_threshold := value > threshold) and (incremented := (new_value := value + 10) > 30):
        results.append(new_value)

print(results)

