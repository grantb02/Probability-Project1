import numpy as np
import matplotlib.pyplot as plt

# Constants
n = 52
sumi = sum(range(1, n + 1))  # Sum of 1 to 52
sumsq = sum(i ** 2 for i in range(1, n + 1))
sqsum = sumi ** 2

n_104 = 104
sumi_104 = sum(range(1, n_104 + 1))
sumsq_104 = sum(i ** 2 for i in range(1, n_104 + 1))
sqsum_104 = sumi_104 ** 2

# Function to calculate r
def calculate_r(deck, n, sumi, sumsq, sqsum):
    iy_sum = sum(i * deck[i - 1] for i in range(1, n + 1))
    return (n * iy_sum - sqsum) / (n * sumsq - sqsum)

# First run: interleaving shuffle
def interleaving_shuffle(deck):
    half = len(deck) // 2
    shuffled_deck = [card for pair in zip(deck[:half], deck[half:]) for card in pair]
    return shuffled_deck

# Second run: alternate starting point shuffle
def alternate_shuffle(deck):
    half = len(deck) // 2
    shuffled_deck = [card for pair in zip(deck[half:], deck[:half]) for card in pair]
    return shuffled_deck

# Run simulation for a given shuffle method
def run_simulation(shuffle_method, n, sumi, sumsq, sqsum):
    original_deck = list(range(1, n + 1))
    deck = original_deck[:]
    r_values = []
    for i in range(15):
        deck = shuffle_method(deck)
        r_values.append(calculate_r(deck, n, sumi, sumsq, sqsum))
    return r_values, deck == original_deck

# First Run (52 cards)
r_values_first, first_returned = run_simulation(interleaving_shuffle, n, sumi, sumsq, sqsum)
# Second Run (52 cards)
r_values_second, second_returned = run_simulation(alternate_shuffle, n, sumi, sumsq, sqsum)
# Third Run (104 cards)
r_values_third, third_returned = run_simulation(interleaving_shuffle, n_104, sumi_104, sumsq_104, sqsum_104)
# Fourth Run (104 cards)
r_values_fourth, fourth_returned = run_simulation(alternate_shuffle, n_104, sumi_104, sumsq_104, sqsum_104)

# Plotting results
def plot_r_values(r_values, title):
    plt.plot(range(1, 16), r_values, marker='o', linestyle='-', color='royalblue')
    plt.xlabel('Number of Shuffles')
    plt.ylabel('Correlation Coefficient (r)')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Plot First Run
plot_r_values(r_values_first, 'First Run (52 cards): Interleaving Shuffles')
# Plot Second Run
plot_r_values(r_values_second, 'Second Run (52 cards): Alternate Shuffles')
# Plot Third Run
plot_r_values(r_values_third, 'Third Run (104 cards): Interleaving Shuffles')
# Plot Fourth Run
plot_r_values(r_values_fourth, 'Fourth Run (104 cards): Alternate Shuffles')

# Questions
print("First Run (52 cards):")
print("1. Minimum r occurs at shuffle:", np.argmin(r_values_first) + 1)
print("2. Cards return to original order:", first_returned)
print("3. Total of 15 runs enough to return to original order:", first_returned)

print("\nSecond Run (52 cards):")
print("1. Minimum r occurs at shuffle:", np.argmin(r_values_second) + 1)
print("2. Cards return to original order:", second_returned)
print("3. Total of 15 runs enough to return to original order:", second_returned)

print("\nThird Run (104 cards):")
print("1. Minimum r occurs at shuffle:", np.argmin(r_values_third) + 1)
print("2. Cards return to original order:", third_returned)
print("3. Total of 15 runs enough to return to original order:", third_returned)

print("\nFourth Run (104 cards):")
print("1. Minimum r occurs at shuffle:", np.argmin(r_values_fourth) + 1)
print("2. Cards return to original order:", fourth_returned)
print("3. Total of 15 runs enough to return to original order:", fourth_returned)
