#!/usr/bin/python3

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append()

    print(result_list)
    return result_list

# or better yet...

def get_primes(input_list):
    print(element for element in input_list if is_prime(element))
    return (element for element in input_list if is_prime(element))

# not germane to the example, but here's a possible implementation of
# is_prime...

def is_prime(number):
    if number > 1:
        if number == 2:
            print('TRUE')
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

print(get_primes(range(1,34)))
