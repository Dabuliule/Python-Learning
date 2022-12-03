motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改
motorcycles[0] = 'ducati'
print(motorcycles)

# 追加
motorcycles.append('honda')
print(motorcycles)

# 插入
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除指定下标处元素
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# 弹出元素并获得
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

# 根据元素的值删除
# remove() 只删除第一个指定的值
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)