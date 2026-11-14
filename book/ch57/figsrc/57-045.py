import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# ligne 1 : départ
box(ax, 2, 66, 84, 14, 'sujet')
text(ax, 44, 75.5, r'$(\eta+\zeta)(x+y)$', 'sujet', 'm')
text(ax, 44, 70.5, 'x = 4, y = 5 : 9 ↦ 18 + 27 = 45', 'sujet', 's')
# ligne 2 : la définition de la somme
box(ax, 2, 50, 84, 10, 'fixe', label=r'$\eta(x+y)+\zeta(x+y)$', size='s')
# ligne 3 : quatre termes
cx = [13, 30, 52, 69]
box(ax, 2, 34, 84, 10, 'fixe')
row3 = [(r'$\eta(x)\ +$', 'fixe', 'normal'), (r'$\eta(y)\ +$', 'varie', 'bold'),
        (r'$\zeta(x)\ +$', 'varie', 'bold'), (r'$\zeta(y)$', 'fixe', 'normal')]
for c, (s, role, w) in zip(cx, row3):
    text(ax, c, 39, s, role, 's', weight=w)
# ligne 4 : deux paquets, les deux termes du milieu ont échangé leur place
box(ax, 3, 8, 38, 10, 'resultat')
box(ax, 45, 8, 38, 10, 'resultat')
row4 = [(r'$(\eta(x)\ +$', 'resultat', 'normal'), (r'$\zeta(x))\ +$', 'varie', 'bold'),
        (r'$(\eta(y)\ +$', 'varie', 'bold'), (r'$\zeta(y))$', 'resultat', 'normal')]
for c, (s, role, w) in zip([13, 30, 52, 69], row4):
    text(ax, c, 13, s, role, 's', weight=w)
# flèches
arrow(ax, (44, 65.5), (44, 60.5), 'fixe', lw=1.0)
text(ax, 48, 63, 'la définition', 'fixe', 's', ha='left')
arrow(ax, (44, 49.5), (44, 44.5), 'fixe', lw=1.0)
text(ax, 48, 47, r'$\eta,\ \zeta$ respectent +', 'fixe', 's', ha='left')
arrow(ax, (30, 33.5), (52, 18.5), 'varie', lw=1.8)
arrow(ax, (52, 33.5), (30, 18.5), 'varie', lw=1.8)
text(ax, 2, 26, 'échange de deux termes', 'varie', 's', ha='left', weight='bold')
save(fig, '57-045')
