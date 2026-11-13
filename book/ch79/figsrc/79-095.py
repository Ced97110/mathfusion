import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
box(ax, 4, 66, 80, 22, 'fixe', label='Départ : $L$, $\\vee$, $\\wedge$\net quatre lois\nL1 commutativité, L2 associativité\nL3 idempotence, L4 absorption', size='s')
steps = [('sujet', r'$\leq$ est un ordre partiel'), ('varie', r'$a\vee b$ : plus petit majorant'), ('autre', r'$a\wedge b$ : plus grand minorant')]
for i, (r, t) in enumerate(steps):
    y = 50 - i * 15
    disc(ax, 9, y + 4, 4, r, label=str(i + 1), size='m'); box(ax, 16, y, 68, 9, r, label=t, size='s')
    arrow(ax, (50, y + 14.5 if i else 65.5), (50, y + 9.5), 'fixe')
box(ax, 4, 3, 80, 9, 'resultat', label='un treillis au sens de l’ordre', size='s'); arrow(ax, (50, 19.5), (50, 12.5), 'fixe')
save(fig, '79-095')
