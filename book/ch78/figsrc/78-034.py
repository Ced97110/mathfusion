import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$x=E,\ y=G,\ a=3$', 'fixe', 'm')
labs = [r'$a(xy)$', r'$(ax)\,y$', r'$x\,(ay)$']
xs = [2, 33, 64]
for i, (x, l) in enumerate(zip(xs, labs)):
    box(ax, x, 46, 22, 10, 'sujet', label=l)
    arrow(ax, (x + 11, 46), (44, 33), 'fixe', lw=0.8)
text(ax, 27.5, 51, '=', 'sujet', 'l'); text(ax, 58.5, 51, '=', 'sujet', 'l')
vals = [['3', '0'], ['0', '0']]
for r in range(2):
    for c in range(2):
        box(ax, 33 + c * 11, 9 + (1 - r) * 11, 11, 11, 'resultat', label=vals[r][c])
text(ax, 62, 20, 'même tableau', 'resultat', 'm', ha='left')
text(ax, 25, 20, 'résultat', 'resultat', 'm', ha='right')
save(fig, '78-034')
