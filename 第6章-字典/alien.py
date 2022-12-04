alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 添加键-值对 / 修改键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['color'] = 'yellow'
print(alien_0)

# 删除键-值对
del alien_0['points']
print(alien_0)