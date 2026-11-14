import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'marches de la base 1 : $1^n$', 'sujet', 'm')
for n in range(6):
    x = 6 + n * 13.5
    box(ax, x, 20, 11, 14, 'sujet', label='1', size='l')
    text(ax, x + 5.5, 14.5, f'$n = {n}$', 'fixe', 's')
    if n < 5: arrow(ax, (x + 11.5, 27), (x + 13, 27), 'varie', lw=0.8)
line(ax, [(6, 37), (6 + 5 * 13.5 + 11, 37)], 'fixe', dash=True)
text(ax, 44, 42, 'toutes les marches : même hauteur', 'resultat', 's')
text(ax, 44, 5, r'aucune marche ne monte : $1^n = 1$', 'resultat', 's')
save(fig, '14-092')
