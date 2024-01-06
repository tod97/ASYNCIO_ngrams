import matplotlib.pyplot as plt

threads = [2, 4, 6, 8, 16, 32]
times = {
   '3.07 MB': [2349, 1999, 1485, 1309, 1331, 1276, 1360],
   '6.15 MB': [5349, 2517, 1669, 1902, 1914, 2018, 2162],
   '12.30 MB': [8626, 4722, 3000, 3353, 3395, 3528, 3748],
   '24.59 MB': [17363, 9462, 5692, 5973, 6239, 6895, 7155],
   '49.18 MB': [34668, 18142, 10704, 11209, 12197, 12575, 13399],
   '98.36 MB': [69099, 36054, 22235, 23906, 24491, 25424, 26777],
   '196.72 MB': [143482, 73893, 46882, 47821, 48477, 51095, 57525],
   '393.44 MB': [280166, 147733, 92635, 93233, 95990, 100494, 116721]}
speedups = {
   '3.07 MB': [1.577, 2.339, 2.048, 1.878, 1.782, 1.608],
   '6.15 MB': [1.95, 2.563, 2.848, 2.551, 2.386, 2.239],
   '12.26 MB': [1.735, 2.91, 2.474, 2.175, 2.218, 1.953],
   '24.59 MB': [1.835, 3.05, 2.907, 2.783, 2.518, 2.426],
   '49.18 MB': [1.911, 3.239, 3.093, 2.842, 2.757, 2.587],
   '98.36 MB': [1.916, 3.108, 2.89, 2.821, 2.718, 2.581],
   '196.72 MB': [1.942, 3.06, 3.0, 2.96, 2.808, 2.494],
   '393.44 MB': [1.896, 3.024, 3.005, 2.919, 2.788, 2.4]
}
colors = ['pink', 'brown', 'purple', 'orange', 'yellow', 'green', 'blue', 'red']

plt.figure(figsize=(10, 8))
for key, time, index in zip(times.keys(), times.values(), range(len(times))):
   plt.plot([1] + threads, time, label=key, color=colors[index])
plt.title('Times')
plt.gcf().canvas.set_window_title('times')
plt.xlabel('Number of threads')
plt.xticks([1] + threads)
plt.ylabel('time (ms)')
plt.legend()

plt.show()


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