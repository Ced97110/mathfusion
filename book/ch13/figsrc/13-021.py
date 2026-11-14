import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 12
f = numberline(ax, 4, 70, y, -4, 2, every=2, arrow_right=False)
line(ax, [(f(-4), y), (f(0), y)], 'sujet', lw=2.2)
disc(ax, f(-2), y, 1.8, 'sujet')
wx = f(-2)
box(ax, wx - 14, 38, 28, 9, 'sujet', label='négatif', size='l', weight='bold')
for i, s in enumerate(('dette de 2 €', '2 degrés sous zéro', '2 m sous la mer')):
    yy = 54 - i * 12
    box(ax, 50, yy - 4, 36, 8, 'fixe', label=s, size='s')
    arrow(ax, (49.5, yy), (wx + 14.5, 42.5 + (1 - i) * 2), 'varie')
arrow(ax, (wx, 37.5), (wx, y + 3), 'sujet')
text(ax, wx - 2, 27, 'à gauche de 0', 'sujet', 's', ha='right')
save(fig, '13-021')
