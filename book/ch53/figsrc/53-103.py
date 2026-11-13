import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
text(ax, 44, 43, 'Le message devient un nombre', 'encre', 'm')
x0, x1, y = 6, 82, 20
f = numberline(ax, x0, x1, y, 0, 54, step=1, labels=False, role='fixe', arrow_right=False, tick=0.8)
text(ax, f(0), y - 4.5, '0', 'fixe', 's')
text(ax, f(54), y - 4.5, '54', 'fixe', 's')
disc(ax, f(8), y, 1.8, 'sujet')
arrow(ax, (f(8), 32), (f(8), y + 3), 'sujet')
text(ax, f(8) + 3, 35, r'$m$ = 8', 'sujet', 'm', ha='left')
text(ax, 44, 8, r'les cases de 0 à $n-1$ = 54', 'fixe', 's')
save(fig, '53-103')
