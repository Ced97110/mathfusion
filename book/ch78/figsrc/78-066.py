import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 2, 42, 38, 12, 'sujet', label=r'$(x^2\circ y)\circ x$')
box(ax, 2, 10, 38, 12, 'sujet', label=r'$x^2\circ(y\circ x)$')
text(ax, 21, 58, 'côté gauche', 'sujet', 's')
text(ax, 21, 6, 'côté droit', 'sujet', 's')
text(ax, 21, 32, r'$x^2$ ne change rien', 'fixe', 's')
arrow(ax, (40, 48), (63.5, 36), 'resultat')
arrow(ax, (40, 16), (63.5, 28), 'resultat')
for (cx, cy, v) in [(66, 32, '0'), (74, 32, '0,5'), (66, 24, '0,5'), (74, 24, '0')]:
    box(ax, cx, cy, 8, 8, 'resultat', label=v)
text(ax, 74, 19, 'même résultat', 'resultat', 's')
save(fig, '78-066')
