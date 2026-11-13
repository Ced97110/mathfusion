import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
w, h, st = 6, 5.5, 6.8
rows = [('A', 10, 44), ('B', 8, 33), ('C', 6, 22)]
def cx(i): return 12 + st * i + w / 2
for name, n, y in rows:
    text(ax, 6, y + h / 2, name, 'encre', 'm')
    for i in range(n):
        role = 'autre' if i == 0 else ('varie' if (i == 1 and name != 'C') else 'fixe')
        box(ax, 12 + st * i, y, w, h, role, r=0.4)
line(ax, [(cx(0), 22 + h), (cx(0), 44)], 'autre', dash=True, lw=1.2)
line(ax, [(cx(1), 33 + h), (cx(1), 44)], 'varie', dash=True, lw=1.2)
text(ax, cx(0), 56, 'Paul', 'autre', 's')
text(ax, cx(1) + 4, 51.5, 'Léa', 'varie', 's')
text(ax, 44, 13, r'$10+8+6=24$ comptés', 'resultat', 'm')
text(ax, 44, 6, 'Léa : 2 fois ; Paul : 3 fois', 'limite', 's')
save(fig, '80-352')
