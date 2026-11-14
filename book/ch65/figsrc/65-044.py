import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(78)
text(ax, 44, 73, 'la preuve en trois temps', 'fixe', 's')
# three steps
box(ax, 2, 48, 25, 20, 'sujet', label='départ :\nun automorphisme', size='s')
box(ax, 31, 46, 28, 24, 'varie', label='étape clé :\nD ≠ −D', size='s', lw=1.8, weight='bold')
box(ax, 63, 48, 23, 20, 'resultat', label='arrivée :\nfixe D ⇔ paire', size='s')
arrow(ax, (27.4, 58), (30.6, 58), 'fixe', lw=0.9)
arrow(ax, (59.4, 58), (62.6, 58), 'fixe', lw=0.9)
# concrete x^3-2
text(ax, 44, 38, r'sur $x^3-2$', 'fixe', 's')
box(ax, 2, 18, 40, 14, 'varie', label='réflexion (impaire) : D → −D', size='s')
box(ax, 46, 18, 40, 14, 'resultat', label='circuit (pair) : D → D', size='s')
text(ax, 22, 11, 'ne fixe pas D', 'varie', 's')
text(ax, 66, 11, 'fixe D', 'resultat', 's')
text(ax, 44, 3.5, r'donc fixer $D$ = fixer $F(D)$', 'sujet', 's')
save(fig, '65-044')
