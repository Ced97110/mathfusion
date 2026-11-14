import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = (30, 48, 66)
box(ax, 4, 48, 14, 12, 'sujet', label='2')
arrow(ax, (18, 54), (28, 54), 'varie')
for x in xs:
    box(ax, x, 48, 16, 12, 'sujet', label='2')
text(ax, 11, 45, '+', 'varie', 'm')
text(ax, 11, 36, r'$g$', 'autre', 'm')
for x, v in zip(xs, (1, 2, 0)):
    box(ax, x, 30, 16, 12, 'autre', label=str(v))
text(ax, 11, 14, r'$g+2$', 'resultat', 'm')
for x, v in zip(xs, (1, 2, 0)):
    box(ax, x, 8, 16, 12, 'resultat', label=str((v + 2) % 3))
save(fig, '55-024')
