import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xs = [2, 18, 34, 50]; labs = [r'$\tau$', r'$-30°$', r'$\tau$', r'$30°$']; heads = [r'$g^{-1}$', r'$h^{-1}$', r'$g$', r'$h$']
roles = ['varie', 'sujet', 'varie', 'sujet']
for x, l, h, r in zip(xs, labs, heads, roles):
    box(ax, x, 30, 14, 10, r, label=l); text(ax, x + 7, 44, h, r, 's')
text(ax, 67.5, 35, '=', 'encre', 'l')
box(ax, 71, 30, 15, 10, 'resultat', label=r'$60°$')
text(ax, 33, 22, r'$g^{-1}h^{-1}gh$ : commutateur', 'encre', 's')
arrow(ax, (78.5, 29), (78.5, 20), 'resultat')
box(ax, 62, 8, 24, 11, 'sujet', label=r'dans $\Omega$')
text(ax, 33, 52, r'$g=\tau$ miroir, $h$ = 30°', 'encre', 's')
save(fig, '73-115')
