import matplotlib.pyplot as plt

core_times = [(1, 92.55), (2, 66.44), (4, 41.11), (8, 26.97), (16, 20.27), (32, 17.56)]

plt.loglog(*zip(*core_times), marker='o', basex=2)
plt.xlabel('Number of Cores')
plt.ylabel('Execution Time (s)')
plt.title('Number of Cores vs. Execution Time')
plt.show()
