import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
text(ax, 44, 69, r'$G_f$ de $x^3-2$ : 6 éléments', 'sujet', 'm', weight='bold')
box(ax, 3, 32, 39, 29, 'resultat')
box(ax, 46, 32, 39, 29, 'varie')
for k, n in enumerate(['1', '(123)', '(132)']):
    disc(ax, 9.5 + k * 13, 50, 5.4, 'resultat')
    text(ax, 9.5 + k * 13, 50, n, 'resultat', 's')
for k, n in enumerate(['(12)', '(13)', '(23)']):
    disc(ax, 52.5 + k * 13, 50, 5.4, 'varie')
    text(ax, 52.5 + k * 13, 50, n, 'varie', 's')
text(ax, 22.5, 38, 'D reste D', 'resultat', 's')
text(ax, 65.5, 38, 'D devient −D', 'varie', 's')
arrow(ax, (22.5, 31), (22.5, 22), 'resultat', lw=1.1)
text(ax, 22.5, 18, r'$G_f\cap A_n$ : 3 paires', 'resultat', 's')
box(ax, 4, 2.5, 37, 8, 'sujet', label=r'corps $F(D)$', size='s')
arrow(ax, (22.5, 14.5), (22.5, 11), 'sujet', lw=0.9)
save(fig, '65-042')
