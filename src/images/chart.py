import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "SimHei"
data = [
    152, 154, 156,
    156, 157, 159,
    160, 160, 162,
    163, 164, 164,
    165, 165, 165,
    166, 167, 167,
    168, 168, 170,
    170, 172, 172,
    173, 174, 176,
    176, 177, 178,
    178, 179, 182,
]

# 频率分布直方图
fig1, axes1 = plt.subplots()
axes1.set_xticks(range(151, 184, 4))
axes1.set_xlabel("身高")
axes1.set_ylabel("频率/组距")
axes1.hist(data, bins=8, density=True, range=(151, 183))
fig1.savefig("chart1.pdf")

# 频率分布折线图
m, n = np.histogram(data, bins=8, range=(151, 183))
y = list(m); y.insert(0, 0); y.append(0)
y = [i / len(data) / 4 for i in y]
x = []
for i in n[:-1]:
    x.append(i + 2)
x.insert(0, x[0] - 4); x.append(x[-1] + 4)
fig2, axes2 = plt.subplots()
axes2.set_xticks(range(147, 188, 4))
axes2.set_xlabel("身高")
axes2.set_ylabel("频率/组距")
axes2.plot(x, y)
fig2.savefig("chart2.pdf")
