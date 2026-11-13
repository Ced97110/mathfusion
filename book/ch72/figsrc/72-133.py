import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 70, r'$B$ ignore le 3e nombre', 'sujet', 'm')
def col(x, titre, role):
    text(ax, x, 60, titre, role, 's')
    line(ax, [(x, 12), (x, 52)], 'fixe')
    for z in (0, 1, 2):
        y = 14 + z * 16
        line(ax, [(x - 1.2, y), (x + 1.2, y)], 'fixe')
        text(ax, x - 4, y, f'{z}', 'fixe', 's', ha='right')
    return lambda z: 14 + z * 16
f = col(24, 'produit de réflexions', 'sujet')
disc(ax, 24, f(1), 1.6, 'sujet')
text(ax, 34, f(1), r'$(0,0,1)$ reste', 'sujet', 's', ha='left')
g = col(64, 'application qui double', 'limite')
disc(ax, 64, g(1), 1.6, 'sujet')
disc(ax, 64, g(2), 1.6, 'limite')
arrow(ax, (64, g(1) + 2), (64, g(2) - 2), 'limite', curve=0)
text(ax, 68, g(2), r'$(0,0,2)$', 'limite', 's', ha='left')
text(ax, 44, 5, 'jamais un produit de réflexions', 'limite', 's')
save(fig, '72-133')
