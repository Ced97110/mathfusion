import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
P = r'$1+1$'
text(ax, 30, 62, r'$6=3\times2+0$', 'encre', 'm')
for x in (3, 19, 35):
    box(ax, x, 48, 14, 9, 'fixe', label=P, size='s')
arrow(ax, (50, 52.5), (64, 52.5), 'varie')
box(ax, 64, 47, 22, 10, 'varie', label=r'$\varphi(6)=0$', size='s')
text(ax, 75, 43, 'dans le noyau', 'varie', 's')
text(ax, 30, 34, r'$7=3\times2+1$', 'encre', 'm')
for x in (3, 19, 35):
    box(ax, x, 20, 14, 9, 'fixe', label=P, size='s')
box(ax, 51, 20, 9, 9, 'varie', label='1')
arrow(ax, (60, 24.5), (64, 24.5), 'varie')
box(ax, 64, 19, 22, 10, 'resultat', label=r'$\varphi(7)=1$', size='s')
text(ax, 44, 8, 'chaque paquet de p = 2 termes vaut 0', 'fixe', 's')
save(fig, '67-042')
