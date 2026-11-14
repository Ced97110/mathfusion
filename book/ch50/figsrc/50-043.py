import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$aP_1a^{-1}$', 'encre', 'xl')
cols = [(15, 'varie', r'$a$', 'tourner'), (44, 'sujet', r'$x\in P_1$', r'élément $x$ de $P_1$'), (73, 'varie', r'$a^{-1}$', 'défaire la rotation')]
for x, role, sym, cap in cols:
    box(ax, x - 12, 46, 24, 11, role, label=sym, size='l')
    arrow(ax, (x, 45.5), (x, 40), role, lw=0.8)
    text(ax, x, 36, cap, role, 's')
    arrow(ax, (x, 32), (44 + (x - 44) * 0.6, 21.5), 'fixe', lw=0.8)
box(ax, 8, 8, 72, 13, 'resultat', label=r'un autre sous-groupe, $P_2$', size='m')
save(fig, '50-043')
