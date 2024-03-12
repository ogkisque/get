import numpy as np
import matplotlib.pyplot as plt

def get_delta(x, y, k):
	n = len(x)
	aver_x = np.mean(x)
	aver_y = np.mean(y)
	aver_x2 = np.mean(x ** 2)
	aver_y2 = np.mean(y ** 2)

	delta_k = (((aver_y2 - aver_y**2) / (aver_x2 - aver_x**2) - k**2) / n) ** 0.5
	delta_b = delta_k * ((aver_x2 - aver_x**2) ** 0.5)
	
	return delta_k, delta_b

y1_arr = np.array([])
x1_arr = np.array([])
y2_arr = np.array([])
x2_arr = np.array([])
y3_arr = np.array([])
x3_arr = np.array([])
i = 1
tmp = []

for line in open("data1.csv"):
	tmp = list(map(float, line.strip().split(";")))
	if i <= 4:
		y1_arr = np.append(y1_arr, tmp[3])
		x1_arr = np.append(x1_arr, tmp[0])
	elif i <= 8:
		y2_arr = np.append(y2_arr, tmp[3])
		x2_arr = np.append(x2_arr, tmp[0])
	else:
		y3_arr = np.append(y3_arr, tmp[3])
		x3_arr = np.append(x3_arr, tmp[0])
	i += 1
	
k1, b1 = np.polyfit(x1_arr, y1_arr, 1)

delta_k1, delta_b1 = get_delta(x1_arr, y1_arr, k1)
print(k1, delta_k1)

k2, b2 = np.polyfit(x2_arr, y2_arr, 1)

delta_k2, delta_b2 = get_delta(x2_arr, y2_arr, k2)
print(k2, delta_k2)

k3, b3 = np.polyfit(x3_arr, y3_arr, 1)

delta_k3, delta_b3 = get_delta(x3_arr, y3_arr, k3)
print(k3, delta_k3)

plt.figure(figsize = (8,6), dpi=150)
plt.ylabel("$\Delta T, K$")
plt.xlabel("$\Delta p, атм$")
plt.grid(True, linestyle="--")
plt.axis([1.3, 4.1, 0.35, 2.8])

x1 = np.array([1.5, 4])
plt.plot(x1, k1 * x1 + b1, "-r", linewidth=1)
plt.errorbar(x1_arr, y1_arr, xerr=0.1, yerr=0.03, fmt="og", ms=3)

x2 = np.array([1.5, 4])
plt.plot(x2, k2 * x2 + b2, "-g", linewidth=1)
plt.errorbar(x2_arr, y2_arr, xerr=0.1, yerr=0.03, fmt="og", ms=3)

x3 = np.array([1.5, 4])
plt.plot(x3, k3 * x3 + b3, "-b", linewidth=1)
plt.errorbar(x3_arr, y3_arr, xerr=0.1, yerr=0.03, fmt="og", ms=3)

plt.show()




