import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 2, 61, r'$(x+h)^4$ : 4 facteurs $(x+h)$', 'encre', 'm', ha='left')
disc(ax, 60, 52, 2.6, 'sujet'); text(ax, 65, 52, '$x$', 'sujet', 's', ha='left')
disc(ax, 74, 52, 2.6, 'varie'); text(ax, 79, 52, '$h$', 'varie', 's', ha='left')
for r in range(4):
    y = 44 - r * 8
    text(ax, 2, y, 'choix %d' % (r + 1), 'fixe', 's', ha='left')
    for c in range(4):
        disc(ax, 36 + c * 14, y, 3, 'varie' if c == r else 'sujet')
box(ax, 8, 4, 72, 11, 'resultat', label=r'4 choix : terme $4x^3h$')
save(fig, '62-095')
