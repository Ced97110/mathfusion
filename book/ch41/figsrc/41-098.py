import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
# notation, découpée en trois morceaux
text(ax, 20, 54, 'proj', 'resultat', 'xl', weight='bold')
text(ax, 29.5, 51.5, r'$v$', 'autre', 'l')
text(ax, 35.5, 54, r'$u$', 'sujet', 'xl')
text(ax, 18, 46, 'la projection', 'resultat', 's')
text(ax, 30, 41.5, 'sur ce vecteur', 'autre', 's')
text(ax, 52, 50, 'de ce vecteur', 'sujet', 's')

o = (10, 6); s = 7
P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
u, v, pr = (1, 3), (4, 2), (2, 1)
arrow(ax, P((0, 0)), P(u), 'sujet')
arrow(ax, P((0, 0)), P(v), 'autre')
arrow(ax, P((0, 0)), P(pr), 'resultat', lw=1.8)
line(ax, [P(u), P(pr)], 'fixe', dash=True)
text(ax, P(u)[0] - 2, P(u)[1] + 1.5, r'$u$', 'sujet')
text(ax, P(v)[0] + 2, P(v)[1] + 1.5, r'$v$', 'autre')
text(ax, 70, 16, r'$\mathrm{proj}_v\,u=\langle 2, 1\rangle$', 'resultat', 's')
text(ax, 70, 9, 'une flèche, pas un nombre', 'encre', 's')
save(fig, '41-098')
