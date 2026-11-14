import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
s = 0.6  # mm par unité
x0 = 10
text(ax, 44, 80, r'$d=-4p^3-27q^2$', 'encre', 'm')
text(ax, 44, 73, r'$p=-3$, $q=1$', 'encre', 's')
box(ax, x0, 58, 108 * s, 9, 'sujet', label=r'$-4p^3=108$')
xe = x0 + 108 * s
box(ax, xe - 27 * s, 40, 27 * s, 9, 'varie', label=r'$-27$')
text(ax, xe - 27 * s - 2, 44.5, r'$-27q^2$', 'varie', 's', ha='right')
line(ax, [(xe - 27 * s, 40), (xe - 27 * s, 21)], 'fixe', lw=0.7, dash=True)
box(ax, x0, 14, 81 * s, 9, 'resultat', label=r'$d=81$')
text(ax, 44, 6, r'$d>0$ : trois racines réelles', 'resultat', 's')
text(ax, 44, 30, r'dernier terme $=9d=729$', 'encre', 's')
save(fig, '69-129')
