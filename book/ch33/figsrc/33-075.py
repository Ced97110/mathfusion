import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, S = 46, 26, 8.0
line(ax, [(ox - 38, oy), (ox + 38, oy)], 'fixe', lw=0.5); line(ax, [(ox, oy - 15), (ox, oy + 30)], 'fixe', lw=0.5)
for sgn in (1, -1): line(ax, [(ox - 36, oy + sgn * 1.5708 * S), (ox + 36, oy + sgn * 1.5708 * S)], 'fixe', lw=0.8, dash=True)
n = 80; xs = [-1 + 2 * i / n for i in range(n + 1)]
line(ax, [(ox + x * S, oy + math.asin(x) * S) for x in xs], 'sujet', lw=1.8)
line(ax, [(ox + x * S, oy + math.acos(x) * S) for x in xs], 'varie', lw=1.8)
xt = [-4.5 + 9 * i / 120 for i in range(121)]
line(ax, [(ox + x * S, oy + math.atan(x) * S) for x in xt], 'resultat', lw=1.8)
for x in (-1, 1):
    disc(ax, ox + x * S, oy + math.asin(x) * S, 0.9, 'sujet'); disc(ax, ox + x * S, oy + math.acos(x) * S, 0.9, 'varie')
    text(ax, ox + x * S, oy - 3, f'{x}'.replace('-', '−'), 'fixe', 's')
text(ax, ox - 37, oy + 1.5708 * S + 2.5, r'$\pi/2$', 'fixe', 's', ha='left'); text(ax, ox - 37, oy - 1.5708 * S - 2.5, r'$-\pi/2$', 'fixe', 's', ha='left')
text(ax, ox - 10, oy + 3.1416 * S, r'$\pi$', 'varie', 's', ha='right')
text(ax, ox - 10, oy - 11, 'arcsin', 'sujet', 'm', ha='right') if False else text(ax, ox - 5, oy - 17.5, 'arcsin', 'sujet', 'm', ha='right')
text(ax, ox - 10, oy + 25, 'arccos', 'varie', 'm', ha='right') if False else text(ax, ox - 12, oy + 22, 'arccos', 'varie', 'm', ha='right')
text(ax, ox + 28, oy + 5, 'arctan', 'resultat', 'm')
save(fig, '33-075')
