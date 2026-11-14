import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 3, 12, 39, 52, 'resultat', fill=False, dash=True)
box(ax, 46, 12, 39, 52, 'limite', fill=False, dash=True)
text(ax, 22.5, 58, 'ℤ : factoriel', 'resultat', 'm', weight='bold')
text(ax, 65.5, 58, 'ℤ[√−5] : non factoriel', 'limite', 's', weight='bold')
for y, s in [(46, r'$12=2\cdot2\cdot3$'), (36, r'$30=2\cdot3\cdot5$'), (26, r'$49=7\cdot7$')]:
    text(ax, 22.5, y, s, 'sujet', 'm')
text(ax, 65.5, 44, r'$6=2\times3$', 'sujet', 'm')
text(ax, 65.5, 33, r'$6=(1+\sqrt{-5})(1-\sqrt{-5})$', 'autre', 's')
text(ax, 22.5, 6, 'chaque élément : 1 écriture', 'resultat', 's')
text(ax, 65.5, 6, '6 : 2 écritures', 'limite', 's')
save(fig, '56-069')
