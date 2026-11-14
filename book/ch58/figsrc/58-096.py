import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 4, 69, 80, 10, 'fixe', label='espace vectoriel : somme, multiple', size='s')
text(ax, 22, 62, r'$\mathbb{R}^2$', 'sujet', 'l', weight='bold')
text(ax, 66, 62, r'$\mathbb{R}^3$', 'sujet', 'l', weight='bold')
text(ax, 22, 55, 'produit ajouté,\npropre à ' + r'$\mathbb{R}^2$', 'varie', 's')
text(ax, 66, 55, 'produit ajouté,\npropre à ' + r'$\mathbb{R}^3$', 'varie', 's')
line(ax, [(44, 6), (44, 62)], 'fixe', lw=0.6, dash=True)
# plan
ox, oy, k = 5, 28, 8
P = lambda a, b: (ox + a * k, oy + b * k)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.5)
text(ax, P(2, 1)[0] + 1.5, P(2, 1)[1] - 2.5, '(2, 1)', 'sujet', 's', ha='left')
text(ax, P(1, 2)[0] - 1.5, P(1, 2)[1] + 2.5, '(1, 2)', 'autre', 's', ha='right')
box(ax, 4, 6, 36, 12, 'resultat', label=r'$2\times1+1\times2=4$' + '\nun nombre', size='s')
# espace
o = (66, 22)
u = 12
arrow(ax, o, iso(1, 0, 0, o, u), 'sujet', lw=1.5)
arrow(ax, o, iso(0, 1, 0, o, u), 'autre', lw=1.5)
arrow(ax, o, iso(0, 0, 1.3, o, u), 'resultat', lw=1.5)
text(ax, iso(1, 0, 0, o, u)[0] + 1.5, iso(1, 0, 0, o, u)[1] - 2.5, r'$u$', 'sujet', 's', ha='left')
text(ax, iso(0, 1, 0, o, u)[0] - 1.5, iso(0, 1, 0, o, u)[1] - 2.5, r'$v$', 'autre', 's', ha='right')
text(ax, o[0] + 2.5, iso(0, 0, 1.3, o, u)[1] - 1, r'$u\times v$', 'resultat', 's', ha='left')
box(ax, 48, 3, 36, 8, 'resultat', label='une flèche', size='s')
save(fig, '58-096')
