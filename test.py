def my_function(num):
    if num == 0:
        return 1
    return num * my_function(num-1)

n = 5
print(my_function(n))