my_foods = ['pizza', 'falafel', 'carrot cake']

# 得到两个列表
friend1_foods = my_foods[:]

# 实际上还是同一个列表
friend2_foods = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend1's favorite foods are:")
print(friend1_foods)

print("\nMy friend2's favorite foods are:")
print(friend2_foods)

my_foods.append('cannoli')
friend1_foods.append('ice-cream')
friend2_foods.append('apple')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend1's favorite foods are:")
print(friend1_foods)

print("\nMy friend2's favorite foods are:")
print(friend2_foods)