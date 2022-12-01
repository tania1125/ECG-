import matplotlib.pyplot as plt
import numpy as np

ecg = np.loadtxt("ecg data.txt")
y = ecg[10:500]
ln = len(y)
x = np.arange(0, ln, 1)
plt.plot(x, y)
#plotted the ecg now going to find index of r phase
maxim = np.max(y)
t = 0.6 * maxim
RX = np.zeros(ln)
RY = np.zeros(ln)
for n in range(ln - 1):
  if y[n] >= t:
    if y[n] > y[n + 1] and y[n] > y[n - 1]:
      RX[n] = n
      RY[n] = y[n]
RX = [i for i in RX if i != 0]
RY = [j for j in RY if j != 0]
print("Index of R peaks in ECG", RX)
#finding index of Q wave
QX = np.zeros(ln)
QY = np.zeros(ln)
lngth = len(RX)
for i in range(lngth):
  l = int(RX[i] - 5)
  u = int(RX[i])

  def num(firstnumber, lastnumber, step=1):
    return range(firstnumber, lastnumber + 1, step)

  for k in num(l, u):
    if y[k] < y[k + 1] and y[k] < y[k - 1]:
      QX[k] = k
      QY[k] = y[k]
      e = max(QY)
      if y[k] == e and y[k + 2] != e:
        QX[k] = k
QX = [w for w in QX if w != 0]
QY = [v for v in QY if v != 0]
print("Index of Q peaks in ECG", QX)
#finding index of S wave
SX = np.zeros(ln)
SY = np.zeros(ln)
lngth = len(RX)
for h in range(lngth):
  lo = int(RX[h] + 5)
  up = int(RX[h])

  def nums(firstnumber, lastnumber, step=1):
    return range(firstnumber, lastnumber + 1, step)

  c = min(y)
  c *= 0.5
  for g in nums(up, lo):
    if y[g] <= c:
      if y[g] < y[g + 1] and y[g] < y[g - 1]:
        SX[g] = g
        SY[g] = y[g]
SX = [a for a in SX if a != 0]
SY = [b for b in SY if b != 0]
print("Index of S peaks in ECG", SX)
