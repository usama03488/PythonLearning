def is_prime(num):
    counter = 0
    for i in range(1, num+1):
        if (num % i == 0):
            counter += 1

    if (counter > 2):
        return False
    else:
        return True
print(is_prime(4))