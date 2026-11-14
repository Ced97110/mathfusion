import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'Dans $\mathbb{Z}[x]$ : diviser $f$ par $g$', 'sujet', 'm')
box(ax, 6, 62, 30, 10, 'sujet', label=r'$f=x^2$')
box(ax, 52, 62, 30, 10, 'sujet', label=r'$g=2x-1$')
text(ax, 44, 52, r'quotient cherché : $q=ax+b$, $a,b$ entiers', 'varie', 's')
text(ax, 44, 44, r'terme dominant de $qg$ : $2a\,x^2$', 'varie', 's')
# droite des valeurs possibles de 2a
f = numberline(ax, 10, 70, 26, 0, 6, step=1, arrow_right=False)
for a in range(0, 4):
    disc(ax, f(2 * a), 26, 1.5, 'varie')
disc(ax, f(1), 26, 1.7, 'limite')
text(ax, f(3), 35, r'valeurs de $2a$ : 0, 2, 4, 6', 'varie', 's')
text(ax, f(1) + 2, 15, r'il faut $2a=1$ : aucun entier', 'limite', 's', ha='left')
arrow(ax, (f(1) + 4, 18), (f(1), 23), 'limite')
save(fig, '54-147')
