import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 17.5, 56, r'dans $\mathbb{F}_9$', 'sujet')
text(ax, 70, 56, r'éléments de $\mathbb{F}_3^*$', 'resultat', 's')
for y, x_lab, n_lab, v in [(38, r'$x=1$', r'$N(x)=1$', '1'), (14, r'$x=1+i$', r'$N(x)=2$', '2')]:
    box(ax, 3, y, 29, 10, 'sujet', label=x_lab)
    arrow(ax, (32, y + 5), (62, y + 5), 'varie')
    text(ax, 47, y + 8.5, n_lab, 'varie', 's')
    disc(ax, 70, y + 5, 8, 'resultat', label=v, size='l')
text(ax, 44, 5, 'les deux valeurs atteintes', 'resultat')
save(fig, '67-166')
