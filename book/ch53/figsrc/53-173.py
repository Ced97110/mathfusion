import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c, x0, top = 5.4, 4, 56
bad = 0
for m in range(55):
    r, col = divmod(m, 11)
    d = (m % 5 == 0 or m % 11 == 0)
    bad += d
    box(ax, x0 + col * c, top - (r + 1) * c, c, c, 'varie' if d else 'fixe', r=0.3, lw=0.5)
assert bad == 15
text(ax, 34, 61, '55 messages, de 0 à 54', 'encre', 'm')
box(ax, 66, 42, 4, 4, 'varie', r=0.3)
text(ax, 72, 44, '15 ont un', 'varie', 's', ha='left')
text(ax, 72, 40.5, 'facteur de 55', 'varie', 's', ha='left')
box(ax, 66, 30, 4, 4, 'fixe', r=0.3)
text(ax, 72, 32, '40 sans', 'fixe', 's', ha='left')
text(ax, 72, 28.5, 'facteur', 'fixe', 's', ha='left')
text(ax, 44, 17, '55 − 40 = 15', 'varie', 'l')
text(ax, 44, 8, '5 + 11 − 1 = 15', 'varie', 'l')
save(fig, '53-173')
