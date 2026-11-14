import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
xs = [3, 34, 65]; w, h, y = 20, 11, 30
vals = [r'$(1,\ 0)$', r'$(2,\ 1)$', r'$(2,\ 3)$']
roles = ['fixe', 'sujet', 'resultat']
caps = ['sac type 1', 'image par η', 'image par ρ']
for x, v, r, c in zip(xs, vals, roles, caps):
    box(ax, x, y, w, h, r, label=v)
    text(ax, x + w / 2, y + h + 3.5, c, r, 's')
for i, nm in enumerate([r'$\eta$', r'$\rho$']):
    x0 = xs[i] + w; x1 = xs[i + 1]
    arrow(ax, (x0 + 0.5, y + h / 2), (x1 - 0.5, y + h / 2), 'varie')
    text(ax, (x0 + x1) / 2, y + h / 2 + 3, nm, 'varie', 'm')
arrow(ax, (xs[0] + w / 2, y - 1), (xs[2] + w / 2, y - 1), 'sujet', curve=0.3)
text(ax, 44, 15, r'$\rho\circ\eta$ : d’abord η, puis ρ', 'sujet', 'm')
save(fig, '58-211')
