import numpy as np
import matplotlib.pyplot as plt

# distribute money = sum to n people
def random_envelope(sum, n):
    envelope = np.zeros(n)
    total = 0
    for i in range(n):
        if i == n - 1:
            envelope[i] = sum - total
            if envelope[i] < 0.01:
                envelope[i] = 0.01
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
    if (sum - total > 1e6 or total - sum > 1e6):
        print("error:", sum - total)
    return envelope

# generate x envelopes with money = sum and give to n people 
def generate_envelopes(sum, n, x):
    envelopes = np.zeros((x, n))
    for i in range(x):
        envelopes[i] = random_envelope(sum, n)
    return envelopes.T

# draw the graph of envelopes, distribute to n people, X times
def draw_envelope_graph(envelopes, n, X):
    mean_n = np.mean(envelopes, axis=1)
    plt.figure(figsize=(10,3))
    plt.xlabel("sequence")
    plt.ylabel("money")
    for i in range(n):
        x = np.random.random(X)
        x = x / 2 + i + 0.75
        plt.scatter(x, envelopes[i], marker='.', alpha=0.5)
    plt.title("All envelopes data scatter plot")
    x_label = range(1, n + 1)
    plt.plot(x_label,mean_n,'c',label='means',markersize=5,markerfacecolor='black',marker='o',markeredgecolor='grey')
    plt.xlabel("squence")
    plt.ylabel("money")
    plt.legend()
    plt.title("Envelopes")
    for i, j in zip(x_label, mean_n):
        plt.text(i, j, '%.2f' % j, ha='center', va='bottom', fontsize=10)
    plt.show()