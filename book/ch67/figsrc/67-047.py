import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
labs = ['termes de somme nulle : 2', 'éléments du petit corps : 2', 'choix par coefficient : 2']
for y, s in zip((50, 36, 22), labs):
    box(ax, 2, y, 52, 9, 'fixe', label=s, size='s')
    arrow(ax, (54, y + 4.5), (63, 37), 'sujet')
box(ax, 63, 25, 23, 24, 'sujet', label=r'$p=2$', size='l')
text(ax, 74.5, 20, 'pour 4 éléments', 'sujet', 's')
text(ax, 44, 11, r'éléments du corps : $p^n$', 'sujet', 'm')
text(ax, 44, 4, r'$p=3$ pour 9 éléments', 'sujet', 's')
save(fig, '67-047')
