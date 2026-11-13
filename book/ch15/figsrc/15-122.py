import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
data = [(46, r'$x=1$', '12', '12', '=', 'accord : rien n\'est prouvé', 'fixe'),
        (14, r'$x=2$', '20', '21', r'$\neq$', 'désaccord : erreur sûre', 'limite')]
for y, xs, a, b, sg, verdict, r in data:
    text(ax, 2, y + 18, xs, 'varie', 'm', ha='left')
    box(ax, 6, y + 2, 30, 12, 'sujet', label=a, size='l')
    box(ax, 52, y + 2, 30, 12, 'autre', label=b, size='l')
    text(ax, 44, y + 8, sg, r, 'l', weight='bold')
    text(ax, 21, y - 1.5, r'$(x+2)(x+3)$', 'sujet', 's'); text(ax, 67, y - 1.5, r'$x^2+6x+5$', 'autre', 's')
    text(ax, 44, y + 18, verdict, r, 's')
save(fig, '15-122')
