import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
xs = [8, 28, 48, 68]
vals = [r'$1$', r'$-3$', r'$-1$', r'$2$']
signs = ['+', '−', '−', '+']
for x, v, s in zip(xs, vals, signs):
    box(ax, x, 16, 14, 12, 'sujet', label=v)
    text(ax, x + 7, 10.5, s, 'encre', 'l')
for i in range(3):
    change = i != 1
    role = 'varie' if change else 'fixe'
    arrow(ax, (xs[i] + 7, 29), (xs[i + 1] + 7, 29), role, curve=-0.6)
    text(ax, xs[i] + 17, 38.5, 'changement' if change else 'aucun', role, 's')
text(ax, 44, 3, 'total : 2 changements', 'resultat', 'm')
save(fig, '69-077')
