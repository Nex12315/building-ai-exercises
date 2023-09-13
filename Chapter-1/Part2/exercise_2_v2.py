portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0],
]

co2 = 0.020

smallest = 1000000
bestroute = None


def permutations(route, ports):
    global smallest, bestroute
    if len(ports) < 1:
        score = co2 * sum(D[i][j] for i, j in zip(route[:-1], route[1:]))
        if score < smallest:
            smallest = score
            bestroute = route
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i + 1 :])


def main():
    permutations([0], list(range(1, len(portnames))))

    print(" ".join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)


main()
