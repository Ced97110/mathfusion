import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 44, 81, r'corps à $q=4$ éléments : $u^4 = u$', 'resultat', 'm')
E = ['0', '1', r'$\alpha$', r'$\alpha+1$']
for k, e in enumerate(E):
    x = 4 + k * 21
    box(ax, x, 60, 19, 10, 'sujet', label=e)
    arrow(ax, (x + 9.5, 59), (x + 9.5, 50), 'varie')
    box(ax, x, 39, 19, 10, 'resultat', label=e)
text(ax, 44, 54.5, 'puissance 4', 'varie', 's')
line(ax, [(2, 32), (86, 32)], 'fixe', dash=True)
text(ax, 44, 26, r'entiers modulo 6 : $2^6 \neq 2$', 'limite', 'm')
box(ax, 4, 6, 18, 10, 'sujet', label='2')
arrow(ax, (23, 11), (32, 11), 'varie')
box(ax, 33, 6, 24, 10, 'limite', label=r'$2^6 = 64$')
arrow(ax, (58, 11), (63, 11), 'varie')
box(ax, 64, 6, 22, 10, 'limite', label=r'reste $4\neq2$', size='s')
save(fig, '67-067')
