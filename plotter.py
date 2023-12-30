import matplotlib.pyplot as plt

threads = [2, 4, 6, 8, 16, 32]
speedups = {
   '3.07 MB': [1.577, 2.339, 2.048, 1.878, 1.782, 1.608],
   '6.15 MB': [1.95, 2.563, 2.848, 2.551, 2.386, 2.239],
   '12.26 MB': [1.735, 2.91, 2.474, 2.175, 2.218, 1.953]
}
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

plt.figure(figsize=(10, 8))

for key, speedup, index in zip(speedups.keys(), speedups.values(), range(len(speedups))):
    plt.plot(threads, speedup, label=key, color=colors[index])

plt.title('Speedups')
plt.gcf().canvas.set_window_title('speedups')
plt.xlabel('Number of threads')
plt.xticks(threads)
plt.ylabel('speedup')
plt.legend()

plt.show()
