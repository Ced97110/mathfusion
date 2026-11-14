import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(42)
y = 20
f = numberline(ax, 14, 72, y, -3, 4, arrow_right=True)
arrow(ax, (14, y), (6, y), 'fixe', lw=0.9)
for v in range(-3, 5):
    disc(ax, f(v), y, 1.6, 'sujet')
disc(ax, f(0.5), y, 1.6, 'autre')
text(ax, f(0.5) + 5, y + 8, '1/2 : entre deux traits', 'autre', 's')
line(ax, [(f(0.5), y + 2), (f(0.5), y + 6)], 'autre', lw=0.6)
brace(ax, f(-3), f(4), y - 7.5, 'sujet', label='les relatifs : un nombre par trait')
text(ax, f(-2.4), y + 8, 'à gauche de 0', 'sujet', 's')
save(fig, '12-072')
