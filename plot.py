import matplotlib.pyplot as plt

core_times = [(1, 125.26), (4, 92.48), (8, 62.39), (16, 12.36), (32, 7.92)]

plt.loglog(*zip(*core_times), marker='o', basex=2)
plt.xlabel('Number of Cores')
plt.ylabel('Time (s)')
plt.title('Number of Cores vs. Execution Time')
plt.show()
