import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'$a\mapsto a^3$ dans $\mathbb{F}_3$', 'encre', 'm')
xs = [16, 42, 66]
labs = [r'$0^3=0$', r'$1^3=1$', r'$2^3=8=2$']
fac = [r'$x$', r'$x-1$', r'$x-2$']
for i, x in enumerate(xs):
    box(ax, x - 6, 54, 12, 9, 'sujet', label=str(i))
    box(ax, x - 6, 28, 12, 9, 'resultat', label=str(i))
    arrow(ax, (x, 53), (x, 38.5), 'varie')
    text(ax, x + 2, 45.5, labs[i], 'varie', 's', ha='left')
    text(ax, x, 21, fac[i], 'sujet', 's')
text(ax, 44, 9, 'chaque élément reste le même', 'resultat', 's')
save(fig, '67-218')
