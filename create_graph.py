import matplotlib.pyplot as plt

threads = [1, 2, 4, 6, 8, 16, 32]
speedup_1 = [0.911, 1.577, 2.339, 2.048, 1.878, 1.782, 1.608]
speedup_2 = [0.973, 1.95, 2.563, 2.848, 2.551, 2.386, 2.239]
speedup_3 = [0.884, 1.735, 2.91, 2.474, 2.175, 2.218, 1.953]

plt.figure(figsize=(10, 8))

plt.plot(threads, speedup_1, marker='o', color='red', label='3.07 MB')
plt.plot(threads, speedup_2, marker='o', color='green', label='6.15 MB')
plt.plot(threads, speedup_3, marker='o', color='blue', label='12.26 MB')

plt.title('Speedups')
plt.xlabel('Number of threads')
plt.xticks(threads)
plt.ylabel('speedup')
plt.legend()

plt.show()
