import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 2, 4, 84, 66, 'fixe')
text(ax, 44, 74.5, r'$S_3$ : 6 rangements possibles', 'fixe', 's')
box(ax, 6, 36, 76, 28, 'resultat')
text(ax, 44, 59.5, r'groupe de $x^3-3x+1$ : $A_3$, 3 éléments', 'resultat', 's')
tops = [('1', 'identité'), (r'$\sigma$', 'circuit'), (r'$\sigma^2$', 'à l’envers')]
for i, (a, b) in enumerate(tops):
    x = 20 + 24 * i
    box(ax, x - 9, 39, 18, 15, 'resultat', fill=False, label=None)
    text(ax, x, 49.5, a, 'resultat', 'l')
    text(ax, x, 42.5, b, 'resultat', 's')
bots = ['$(r_1\\ r_2)$', '$(r_1\\ r_3)$', '$(r_2\\ r_3)$']
for i, a in enumerate(bots):
    x = 20 + 24 * i
    box(ax, x - 9, 9, 18, 15, 'limite', label=a, size='m', dash=True)
text(ax, 44, 29, 'échanges de deux racines : absents', 'limite', 's')
save(fig, '65-012')
