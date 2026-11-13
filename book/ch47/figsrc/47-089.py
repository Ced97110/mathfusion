import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'horloge à 12 heures', 'fixe', 's')
X = lambda v: 12 + v * 6.2
for name, y, role, S in [('H', 58, 'sujet', {0, 6}), ('K', 40, 'autre', {0, 4, 8})]:
    text(ax, 4, y, name, role, 'l')
    for v in range(12):
        disc(ax, X(v), y, 2.7, role if v in S else 'fixe', fill=v in S, label=str(v), size='s')
for v in (4, 8):
    arrow(ax, (X(v), 37), (X(v), 31), 'limite')
    line(ax, [(X(v) - 2, 61), (X(v) + 2, 55)], 'limite', lw=1.0) if False else None
text(ax, 44, 26.5, r'4 et 8 ne sont pas dans $H$', 'limite', 's')
text(ax, 44, 66.5, r'$[G:H]=6$   $[G:K]=4$', 'encre', 'm')
text(ax, 44, 14, r'$6\times[H:K]=4$ : impossible', 'limite', 'm')
text(ax, 44, 7.5, r'il faut $K\subseteq H\subseteq G$', 'resultat', 's')
save(fig, '47-089')
