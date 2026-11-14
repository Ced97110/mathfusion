import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 49, r'$30=2\times3\times5$', 'sujet', 'l')
for x, p in ((10, 2), (36, 3), (62, 5)):
    box(ax, x, 32, 16, 9, 'sujet', label=rf'${p}^1$')
    arrow(ax, (x + 8, 31.5), (x + 8, 26), 'varie')
    text(ax, x + 8, 22.5, r'$P(1)=1$', 'resultat', 's')
    line(ax, [(x + 8, 20), (x + 8, 17)], 'fixe')
line(ax, [(18, 17), (70, 17)], 'fixe')
arrow(ax, (44, 17), (44, 13), 'fixe')
box(ax, 8, 3, 72, 9.5, 'resultat', label=r'$1\times1\times1=1$ groupe : $\mathbb{Z}/30$')
save(fig, '60-242')
