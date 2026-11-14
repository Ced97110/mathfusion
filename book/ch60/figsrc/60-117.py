import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'$G=\mathbb{Z}/12$ , $p=3$ , $H=\{0,6\}$', 'encre', 's')
labs1 = [r'$a=2$', r'$2a=4$', r'$3a=6$']
labs2 = [r'$ra=4$', r'$2ra=8$', r'$3ra=12$']
xs = [14, 38, 62]
for x, l in zip(xs, labs1):
    box(ax, x, 44, 20, 10, 'sujet' if l != labs1[2] else 'fixe', label=l, size='s')
for x, l in zip(xs, labs2):
    box(ax, x, 14, 20, 10, 'resultat', label=l, size='s')
text(ax, 8, 49, 'a', 'sujet', 'm')
text(ax, 8, 19, 'ra', 'resultat', 'm')
text(ax, 44, 39, r'$3a=6$ est dans $H$, pas nul', 'sujet', 's')
arrow(ax, (24, 43), (24, 25), 'varie')
text(ax, 28, 34, r'multiplier par $r=2$', 'varie', 's', ha='left')
text(ax, 44, 8, r'$3\times 4=12=0$ : ordre 3', 'resultat', 's')
save(fig, '60-117')
