# use a recursive algorithm to find a maximum, minimum, and sum value


# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 97, 41, 49, 53]

print("Find Max Value")
def find_max(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    val1 = items[0]
    val2 = find_max(items[1:])
    print(val1, val2)

    # perform the comparison when we're down to just two
    if val1 > val2:
        return val1
    else:
        return val2


# test the function
print(find_max(items))

print("Find Min Value")
def find_min(items):
    # breaking condition: last item in list? return it
    if len(items) == 1:
        return items[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    val1 = items[0]
    val2 = find_min(items[1:])
    print(val1, val2)

    # perform the comparison when we're down to just two
    if val1 < val2:
        return val1
    else:
        return val2
    

# test the function
print(find_min(items))

print("Find Sum")
def find_sum(items):
    # breaking condition: list is empty? return 0
    if len(items) == 0:
        return 0

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    val = items[0]
    rest = items[1:]
    print(val, rest)

    # perform the addition
    return val + find_sum(rest)


# test the function
print(find_sum(items))