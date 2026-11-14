import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 22
f = numberline(ax, 14, 72, y, -3, 4, arrow_right=True)
arrow(ax, (14, y), (6, y), 'fixe', lw=0.9)
for v in range(-3, 5):
    disc(ax, f(v), y + 5, 2, 'varie' if v == -2 else ('sujet' if v >= 0 else 'fixe'))
arrow(ax, (f(0), y + 8), (f(-2), y + 8), 'varie', curve=0.5)
text(ax, f(-1), y + 17, '2 pas à gauche de 0', 'varie', 's')
brace(ax, f(0), f(4), y - 6.5, 'sujet', label='entiers')
text(ax, f(-2), y - 7, '−2 : pas un entier', 'limite', 's')
save(fig, '12-074')
