def replace_value(values, index, new_value):
    values[index] = new_value
    return

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            values[i] = target
            return i
    return -1

def summarize(values):
    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    return minimum, maximum, total

days = int(input("The number of days: "))

original = []

for i in range(days):
    minute = int(input(f"Time spend reading on day {i+1}: "))
    original.append(minute)

updated = original[:]

index = int(input("Index to replace: "))
new_value = int(input("Reading time (in minutes): "))

replace_value(updated, index, new_value)

target = int(input("What is one of the times you spent reading: "))

find_first(updated, target)
variable = find_first(updated, target)

summarize(updated)
minimum, maximum, total = summarize(updated)

another_list = sorted(updated)

print(f"Original list: {original}")
print(f"Updated list: {updated}")
print(f"Sorted list: {another_list}")
print(f"Smallest reading time: {minimum} minutes")
print(f"Largest reading time: {maximum} minutes")
print(f"Total reading time: {total} minutes")
if variable == -1:
    variable = "Target not found"
    print(variable)
else:
    print(f"First matching index: {variable}")

matching = updated.count(new_value)

print(f"Matching values: {matching}")