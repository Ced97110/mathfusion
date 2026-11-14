import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 2, 4, 84, 66, 'resultat')
text(ax, 44, 74.5, r'groupe de $x^3-2$ : $S_3$, $3\times2\times1=6$', 'resultat', 's')
tops = [('1', 'identité'), (r'$\sigma$', 'circuit'), (r'$\sigma^2$', 'à l’envers')]
for i, (a, b) in enumerate(tops):
    x = 20 + 24 * i
    box(ax, x - 9, 38, 18, 24, 'resultat', fill=False)
    text(ax, x, 55, a, 'resultat', 'l')
    text(ax, x, 46, b, 'resultat', 's')
text(ax, 44, 66.5, 'dont $A_3$ (3 éléments)', 'resultat', 's')
bots = ['$(r_1\\ r_2)$', '$(r_1\\ r_3)$', '$(r_2\\ r_3)$']
for i, a in enumerate(bots):
    x = 20 + 24 * i
    box(ax, x - 9, 9, 18, 15, 'resultat', fill=False, label=a, size='m')
text(ax, 44, 29, '+ 3 échanges de deux racines : présents', 'resultat', 's')
save(fig, '65-018')
