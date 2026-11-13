import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = lambda v: 12 + (v - 1) * 9.2
y1, y2 = 42, 18
text(ax, 4, y1 + 9, 'diviseurs de 8', 'sujet', 's', ha='left')
text(ax, 4, y2 + 9, 'multiples de 2', 'resultat', 's', ha='left')
for v in range(1, 9):
    ax.plot([f(v)] * 2, [y1 - 1.2, y1 + 1.2], color=COL['fixe'], lw=0.5)
    ax.plot([f(v)] * 2, [y2 - 1.2, y2 + 1.2], color=COL['fixe'], lw=0.5)
line(ax, [(f(1) - 4, y1), (f(8) + 4, y1)], 'fixe', lw=0.5); line(ax, [(f(1) - 4, y2), (f(8) + 4, y2)], 'fixe', lw=0.5)
for v in (1, 2, 4, 8):
    disc(ax, f(v), y1, 3.2, 'fixe' if v == 1 else 'sujet', label=str(v), size='m')
for v in (2, 4, 6, 8):
    disc(ax, f(v), y2, 3.2, 'resultat', label=str(v), size='m')
for v in (2, 4, 8):
    arrow(ax, (f(v), y1 - 3.8), (f(v), y2 + 3.8), 'varie', lw=0.8)
text(ax, f(1), y1 - 8, '1 exclu', 'fixe', 's')
text(ax, W / 2, 5, 'les autres diviseurs : multiples de 2', 'varie', 'm')
save(fig, '49-187')
