import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s = 4.6
gx, gy = 16, 10
for i in range(2):
    for j in range(10):
        hl = (i == 1 and j == 7)
        box(ax, gx + i * s, gy + j * s, s, s, 'varie' if hl else 'fixe', r=0.2)
for i in range(2):
    text(ax, gx + (i + 0.5) * s, gy - 3, str(i), 'sujet', 's')
for j in (0, 3, 6, 9):
    text(ax, gx - 3, gy + (j + 0.5) * s, str(j), 'autre', 's')
text(ax, gx + s, gy + 10 * s + 4, 'u', 'sujet', 'm', weight='bold')
text(ax, gx - 9, gy + 5 * s, 'v', 'autre', 'm', weight='bold')
hx, hy = gx + 1.5 * s, gy + 7.5 * s
arrow(ax, (56, 53), (hx + 2.5, hy + 0.5), 'varie', lw=1.0)
text(ax, 68, 55, '1·y₁ + 7·y₂', 'varie', 's')
text(ax, 68, 40, '2 × 10 = 20 cases', 'fixe', 's')
text(ax, 68, 34, '1 élément', 'fixe', 's')
text(ax, 68, 29, '= 1 seule case', 'fixe', 's')
save(fig, '59-101')
