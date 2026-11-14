import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
# départ
box(ax, 2, 72, 84, 14, 'sujet', label='départ : $V$ avec $T$ linéaire\n$v$ = (2 ; 1)', size='s')
# étape clé, nommée sur la flèche et vérifiée sur le cas chiffré
arrow(ax, (44, 71.5), (44, 59.5), 'varie', lw=1.8)
text(ax, 49, 65.5, 'étape clé :\n$T$ commute avec\nles nombres de $F$', 'varie', 's', ha='left', weight='bold')
box(ax, 2, 46, 84, 12, 'varie', lw=1.6, label='$T$(3$v$) = 3($Tv$) = (−3 ; 6)', size='s')
# on peut mettre T à la place de x
arrow(ax, (44, 45.5), (44, 36.5), 'fixe', lw=1.2)
text(ax, 49, 41, 'on remplace $x$ par $T$', 'fixe', 's', ha='left')
text(ax, 44, 31, 'arrivée : les 4 règles tiennent', 'resultat', 's', weight='bold')
box(ax, 2, 6, 38, 18, 'resultat', label='$(x+2)$ puis $(x+1)$\n(3 ; 4) puis (−1 ; 7)', size='s')
box(ax, 48, 6, 38, 18, 'resultat', label='$(x^2+3x+2)$ d’un coup\n(−1 ; 7)', size='s')
text(ax, 44, 15, '=', 'resultat', 'xl', weight='bold')
save(fig, '57-099')
