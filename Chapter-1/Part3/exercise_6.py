import numpy as np
import random
import math

N = 100  # size of the problem is N x N
steps = 3000  # total number of iterations
tracks = 50


# generate a landscape with multiple local optima
def generator(x, y, x0=0.0, y0=0.0):
    return (
        np.sin((x / N - x0) * np.pi)
        + np.sin((y / N - y0) * np.pi)
        + 0.07 * np.cos(12 * (x / N - x0) * np.pi)
        + 0.07 * np.cos(12 * (y / N - y0) * np.pi)
    )


x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)


def main():
    global x
    global y

    for step in range(steps):
        # Temperature schedule
        T = max(0, ((steps - step) / steps) ** 3 - 0.005)

        # Update solutions on each search track
        for i in range(tracks):
            # Try a new solution near the current one
            x_new = np.random.randint(max(0, x[i] - 2), min(N, x[i] + 2 + 1))
            y_new = np.random.randint(max(0, y[i] - 2), min(N, y[i] + 2 + 1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # Simulated annealing acceptance criteria
            if S_new > S_old:
                x[i], y[i] = x_new, y_new  # New solution is better, go there
            else:
                # Calculate acceptance probability
                if T > 0:  # Avoid division by zero
                    accept_prob = math.exp((S_new - S_old) / T)
                    if random.random() < accept_prob:
                        x[i], y[i] = (
                            x_new,
                            y_new,
                        )  # Accept new solution with calculated probability

    # Number of tracks that found the peak
    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)]))


main()
