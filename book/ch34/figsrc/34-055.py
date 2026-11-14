import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 70 / 225; x0 = 9
a = 167 * u; b = 58 * u
box(ax, x0, 34, a, 8, 'sujet', label='167,0', size='s'); box(ax, x0 + a, 34, b, 8, 'varie', label='58,0', size='s')
text(ax, x0 + a / 2, 47, r'$p^2\sin^2(A+B)$', 'sujet', 's'); text(ax, x0 + a + b / 2 + 2, 47, r'$p^2\cos^2(A+B)$', 'varie', 's')
arrow(ax, (x0 + 35, 31), (x0 + 35, 21), 'fixe')
text(ax, x0 + 38, 26, r'$\sin^2+\cos^2=1$', 'fixe', 's', ha='left')
box(ax, x0, 11, 70, 8, 'resultat', label='p² = 225 = 15²', size='s')
save(fig, '34-055')
