def is_prime(func):
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs) == int or float:
            print("Простое ")
        else:
            print("Составное")
        return func(*args, **kwargs)
    return wrapper


@is_prime
def sum_three(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1


result = sum_three(2, 3, 6)
print(result)
