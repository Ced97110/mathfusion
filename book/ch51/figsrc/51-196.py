import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'cadran à 4 h : $x=x+x$ ?', 'encre', 'm')
data = [(0, 0, True), (1, 2, False), (2, 0, False), (3, 2, False)]
for i, (x, s, ok) in enumerate(data):
    y = 61 - i*11
    box(ax, 6, y - 4.5, 56, 9, 'resultat' if ok else 'fixe', label=rf'$x={x}$ : $x+x={s}$', size='m')
    text(ax, 72, y, '✓' if ok else '✗', 'resultat' if ok else 'limite', 'l', weight='bold')
arrow(ax, (44, 20), (44, 14), 'varie')
box(ax, 14, 2, 60, 11, 'sujet', label=r'$x=0\cdot a$ donc $x=0$', size='m')
save(fig, '51-196')
