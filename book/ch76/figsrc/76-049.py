import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [3, 33, 63]; wd = 22
box(ax, xs[0], 38, wd, 10, 'sujet', label='(4 ; 0)')
box(ax, xs[1], 38, wd, 10, 'varie', label='(3 ; 7)')
box(ax, xs[2], 38, wd, 10, 'resultat', label='(12 ; 0)')
text(ax, 29, 43, r'$\times$', 'encre', 'l'); text(ax, 59, 43, '=', 'encre', 'l')
text(ax, xs[0] + 11, 53, 'dans le noyau', 'sujet', 's')
text(ax, xs[1] + 11, 53, 'quelconque', 'varie', 's')
text(ax, xs[2] + 11, 53, 'reste dedans', 'resultat', 's')
for x, v, r in zip(xs, ['0', '7', '0'], ['sujet', 'varie', 'resultat']):
    arrow(ax, (x + 11, 37), (x + 11, 22), 'fixe')
    text(ax, x + 13.5, 29.5, r'$\eta$', 'fixe', 's', ha='left')
    box(ax, x + 3, 10, 16, 10, r, label=v)
text(ax, 44, 4, 'seconde case : 0 pour le noyau', 'fixe', 's')
save(fig, '76-049')
