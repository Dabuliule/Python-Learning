name = "ada lovelace"

# 首字母大写
print(name.title())

# 全部大写
print(name.upper())

# 全部小写
print(name.lower())

# 合并字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello," + full_name.title() + "!")
message = "Hello," + full_name.title() + "!"
print(message)

favorite_language = ' python '
# 删除字符串后面的空白
print(favorite_language.rstrip())

# 删除字符串前面的空白
print(favorite_language.lstrip())

# 删除字符串中所有的空白
print(favorite_language.strip())