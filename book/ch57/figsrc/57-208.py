import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 20, 61, r'horloge $\mathbb{Z}/6\mathbb{Z}$', 'sujet', 'm')
for i, (e, o) in enumerate((('1', '6'), ('2', '3'), ('3', '2'))):
    box(ax, 4 + i * 27, 44, 25, 10, 'resultat', label=f'{e} : ordre {o}', size='s')
text(ax, 44, 38, 'ordres 6, 3, 2 : ils divisent 6 et 12', 'resultat', 's')
line(ax, [(4, 32), (84, 32)], 'fixe', lw=0.6, dash=True)
text(ax, 22, 26, r'$\mathbb{Z}/4\mathbb{Z}$ avec $n=2$', 'limite', 'm')
box(ax, 4, 9, 25, 10, 'limite', label='1 : ordre 4', size='s')
text(ax, 58, 14, '4 ne divise pas 2 :', 'limite', 's')
text(ax, 58, 9.5, 'pas un module sur ℤ/2ℤ', 'limite', 's')
save(fig, '57-208')
