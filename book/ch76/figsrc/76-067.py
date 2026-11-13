import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, r'$n=4,\ r=2$', 'sujet', 'm')
for i in range(4): disc(ax, 20 + i * 16, 55, 3.4, 'sujet', label=str(i + 1))
arrow(ax, (44, 50), (44, 44), 'varie')
text(ax, 44, 41, 'parties à 2 éléments', 'varie', 's')
pairs = ['12', '13', '14', '23', '24', '34']
for k, pr in enumerate(pairs):
    box(ax, 7 + (k % 3) * 26, 26 - (k // 3) * 11 + 0, 24, 9, 'sujet', label=rf'$e_{{{pr}}}$')
arrow(ax, (44, 15), (44, 11), 'varie')
box(ax, 22, 1.5, 44, 9, 'resultat', label=r'$\binom{4}{2}=6$ parties', size='m')
save(fig, '76-067')
