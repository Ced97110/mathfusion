import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def S(*c): return r'$\{' + ','.join(c) + r'\}$'
w, h = 18, 8
box(ax, 4, 28, w, h, 'sujet', label=S('r', 'b')); box(ax, 66, 28, w, h, 'autre', label=S('b', 'v'))
box(ax, 35, 50, w, h, 'resultat', label=S('r', 'b', 'v')); box(ax, 35, 6, w, h, 'resultat', label=S('b'))
for (p, q) in [((13, 36), (38, 50)), ((75, 36), (50, 50)), ((38, 14), (13, 28)), ((50, 14), (75, 28))]:
    line(ax, [p, q], 'resultat', lw=1.6)
text(ax, 44, 61, 'union : la plus petite au-dessus', 'resultat', 's') if False else None
text(ax, 4, 56, 'union', 'resultat', 'm', ha='left'); text(ax, 4, 10, 'intersection', 'resultat', 'm', ha='left')
text(ax, 62, 56, 'plus petite au-dessus', 'resultat', 's', ha='left') if False else None
text(ax, 44, 40, 'pas de lien', 'limite', 's')
save(fig, '79-006')
