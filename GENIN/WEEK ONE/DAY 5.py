fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits) 

student_heights = input("Input a list of student heights\n"). split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)
average_height = round(total_height / number_of_students)
print(average_height)

student_scores = [78, 65, 87, 90, 91, 64, 89]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
total = 0
for number in range(1, 101):
    total += number
print(total)