import random

# Part A
weeks = 16
classes = 5
tuition = 6000
classes_per_week = 3
cost_per_week = (tuition / classes) / weeks
cost_per_class = (cost_per_week/classes_per_week)
print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class)

print("weeks = ", weeks, type(weeks))
print("classes = ", classes, type(classes))
print("tuition = ", tuition, type(tuition))
print("classes per week = ", classes_per_week, type(classes_per_week))
print("cost per week is", cost_per_week, type(cost_per_week))
print("cost per class is", cost_per_class, type(cost_per_class))

#Part B
rand_list = [1, 2, 3, 4, 5]
rand_number = random.choice(rand_list)
print("your random number is:", rand_number)