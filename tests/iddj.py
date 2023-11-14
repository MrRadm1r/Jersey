from matplotlib import pyplot as plt
import math
s = 0
x = list(range(0, 20))
y = []
for k in x:
    for i in range(1, k+1):
        for j in range(1, k+1):
            s += (i//j)
    y.append(s)
    s = 0

plt.plot(x, y, color='red')
plt.plot(x[::len(x)-1], y[::len(y)-1], color='blue', linestyle='--')
print(math.degrees(math.atan(x[-1]/y[-1])))
plt.show()
