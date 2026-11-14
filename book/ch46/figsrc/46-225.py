import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'$sg(\sigma)$ : « signature de $\sigma$ »', 'encre', 'm')
for y, p, par, v in [(30, '(1 2 3)', 'paire', r'$sg(\sigma)=+1$'), (10, '(1 2)', 'impaire', r'$sg(\sigma)=-1$')]:
    box(ax, 3, y - 5, 24, 10, 'sujet', label=p)
    text(ax, 40, y + 3.5, par, 'varie', 's')
    arrow(ax, (28, y), (51, y), 'varie')
    box(ax, 52, y - 5, 33, 10, 'resultat', label=v)
save(fig, '46-225')
