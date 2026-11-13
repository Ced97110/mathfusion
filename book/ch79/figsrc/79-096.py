import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
for y, h, l in ((70, 'réflexivité', 'L3 : idempotence'), (52, 'antisymétrie', 'L1 : commutativité'), (34, 'transitivité', 'L2 : associativité')):
    text(ax, 2, y, h, 'sujet', 's', ha='left'); text(ax, 86, y, l, 'fixe', 's', ha='right')
text(ax, 44, 63, r'$4\vee4=4$ donc $4\leq4$', 'resultat', 's')
text(ax, 44, 45, r'$a\leq b$ et $b\leq a$ : $a=b$', 'resultat', 's')
for x, n in ((30, '4'), (44, '12'), (58, '60')): disc(ax, x, 12, 4, 'sujet', label=n, size='s')
arrow(ax, (34.4, 12), (39.6, 12), 'varie'); arrow(ax, (48.4, 12), (53.6, 12), 'varie')
arrow(ax, (30, 16.5), (58, 16.5), 'resultat', lw=1.2, curve=-0.4)
save(fig, '79-096')
