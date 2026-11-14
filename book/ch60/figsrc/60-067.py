import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(65)
line(ax, [(37, 10), (37, 60)], 'fixe', dash=True)
text(ax, 20, 59, 'ℤ/2 : scalaire 1', 'sujet', 's')
text(ax, 62, 59, 'ℤ/4 : scalaire 2, jamais 1', 'sujet', 's')
yS, yT, h, w = 44, 18, 7, 8
# left panel
lx = [10, 22]
for i in range(2):
    box(ax, lx[i], yS, w, h, 'sujet', label=str(i))
    box(ax, lx[i], yT, w, h, 'resultat', label=str(i))
    arrow(ax, (lx[i] + w / 2, yS), (lx[i] + w / 2, yT + h), 'varie')
# right panel
rx = [44, 55, 66, 77]
for i in range(4):
    box(ax, rx[i], yS, w, h, 'sujet', label=str(i))
roles = ['sujet', 'limite', 'sujet', 'fixe']
for i in range(4):
    box(ax, rx[i], yT, w, h, roles[i], label=str(i))
for i in range(4):
    j = (2 * i) % 4
    arrow(ax, (rx[i] + w / 2, yS), (rx[j] + w / 2, yT + h), 'varie')
save(fig, '60-067')
