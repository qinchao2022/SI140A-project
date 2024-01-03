import numpy as np

# distribute money = sum to n people
def random_envelope(sum, n):
    envelope = np.zeros(n)
    total = 0
    for i in range(n):
        if i == n - 1:
            envelope[i] = sum - total
            total += envelope[i]
            break
        max = (sum - total) * 200 / (n - i)
        money = np.random.randint(1, max + 1) / 100
        if money < 0.01:
            money = 0.01
        envelope[i] = money
        total += money
        if envelope[i] >= sum or envelope[i] < 0.01 or total > sum:
            print("error")
    if (sum - total >1e8):
        print("error:", sum - total)
    return envelope

# generate x envelopes with money = sum and give to n people 
def generate_envelopes(sum, n, x):
    envelopes = np.zeros((x, n))
    for i in range(x):
        envelopes[i] = random_envelope(sum, n)
    return envelopes.T