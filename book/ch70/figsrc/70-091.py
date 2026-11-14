import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 44, 37, 14, 'sujet', label=r'$\forall x,\ x^2+1>0$')
text(ax, 44, 51, '=', 'encre', 'xl')
box(ax, 49, 44, 37, 14, 'sujet', label=r'non, $\exists x$, non($x^2+1>0$)')
text(ax, 44, 38, 'on essaie des nombres $x$', 'fixe', 's')
for i, (x, v) in enumerate([(-1, 2), (0, 1), (1, 2)]):
    bx = 2 + 29 * i
    box(ax, bx, 20, 26, 12, 'resultat', label=r'$x=%d$ : $%d>0$' % (x, v))
    arrow(ax, (bx + 13, 44), (bx + 13, 33.5), 'fixe', lw=0.6)
text(ax, 44, 10, 'aucun $x$ ne la rend fausse', 'resultat', 'm')
save(fig, '70-091')
