portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0],
]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020
smallest = 1_000_000
bestroute = [0, 0, 0, 0, 0]

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them


def generate_permutation(arr, start, result):
    if start == len(arr) - 1:
        result.append(arr.copy())

    for i in range(start, len(arr)):
        # Swap elements at start and i
        arr[start], arr[i] = arr[i], arr[start]

        # Recursively generate permutations for the rest of the array
        generate_permutation(arr, start + 1, result)

        # Swap back to backtrack and try other possibilities
        arr[start], arr[i] = arr[i], arr[start]


def permutations(route, ports):
    # Write your recursive code here
    result = []
    generate_permutation(ports, 0, result)
    for el in result:
        el.insert(0, route[0])

    return result


def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing
    global smallest
    global bestroute
    global co2

    # this will start the recursion
    options = permutations([0], list(range(1, len(portnames))))

    for option in options:
        length = 0
        for i in range(len(option)):
            if i < len(option) - 1:
                length += D[option[i]][option[i + 1]] * co2
        if smallest > length:
            smallest = length
            bestroute = option

    # print the best route and its emissions
    print(" ".join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)


main()
