marks = [78, 85, 62, 90, 73, 88, 95, 67]

average = sum(marks) / len(marks)

print(f"Average marks: {average:.2f}")
print("Students with marks above average:")

for mark in marks:
    if mark > average:
        print(mark)