import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# le plan (départ)
box(ax, 3, 20, 32, 36, 'sujet')
ox, oy = 19, 38
line(ax, [(5, oy), (33, oy)], 'fixe')
for xv in (8, 13, 25, 30):
    line(ax, [(xv, 22), (xv, 54)], 'fixe', lw=0.6, dash=True)
line(ax, [(ox, 22), (ox, 54)], 'varie', lw=2.0)
text(ax, ox + 2, 51, 'noyau', 'varie', 's', ha='left')
text(ax, 19, 15, 'plan : dimension 2', 'sujet', 's')
text(ax, 19, 10, 'noyau : dimension 1', 'varie', 's')
# la règle (p ; q) -> p
arrow(ax, (37, 38), (51, 38), 'fixe')
text(ax, 44, 43, r'$(p\,;\,q)\mapsto p$', 'encre', 's')
# l'image : la droite réelle
line(ax, [(53, 38), (83, 38)], 'resultat', lw=2.0)
for xv in (58, 68, 78):
    line(ax, [(xv, 36.5), (xv, 39.5)], 'resultat', lw=0.8)
text(ax, 68, 32, r'image : $\mathbb{R}$', 'resultat', 's')
text(ax, 68, 27, 'dimension 1', 'resultat', 's')
text(ax, 68, 14, '2 = 1 + 1', 'encre', 'l', weight='bold')
save(fig, '57-181')
