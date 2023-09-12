portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


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

    # Print the port names in route when the recursion terminates
    for el in result:
        print(" ".join([portnames[i] for i in el]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
