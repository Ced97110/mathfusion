import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s = 12.0
r3 = math.sqrt(3)
ox, oy = 28.0, 36.0
P = lambda a, b: (ox + a * s, oy + b * r3 * s)
arrow(ax, (ox - 26, oy), (ox + 30, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 29), (ox, oy + 31), 'fixe', lw=0.7)
t = [i * math.pi / 60 for i in range(121)]
line(ax, [(ox + 2 * s * math.cos(a), oy + 2 * s * math.sin(a)) for a in [i * math.pi / 30 for i in range(61)]], 'fixe', lw=0.7, dash=True)
for name, (a, b), pos in [('2', (2, 0), (2.4, -3.2)), ('p1', (1, 1), (1.0, 3.5)), ('p2', (1, -1), (1.0, -3.5))]:
    x, y = P(a, b)
    disc(ax, x, y, 1.6, 'varie')
x1, y1 = P(1, 1)
line(ax, [(ox, oy), (x1, y1)], 'varie')
line(ax, [(x1, oy), (x1, y1)], 'fixe', dash=True)
text(ax, ox + 2 * s + 2.5, oy + 3, '2', 'varie', 's', ha='left')
text(ax, x1 - 1.5, y1 + 3.5, r'$1+\sqrt{3}\,i$', 'varie', 's', ha='right')
text(ax, P(1, -1)[0] - 1.5, P(1, -1)[1] - 3.5, r'$1-\sqrt{3}\,i$', 'varie', 's', ha='right')
text(ax, ox - 1.5, oy + 12, 'distance 2', 'fixe', 's', ha='right')
text(ax, 60, 66, 'ν = a² + 3b²', 'sujet', 'm', ha='left')
text(ax, 60, 52, 'ν(2) = 4 + 0 = 4', 'encre', 's', ha='left')
text(ax, 60, 44, r'$\nu(1\pm\sqrt{3}\,i)=1+3=4$', 'encre', 's', ha='left')
text(ax, 60, 36, 'carré de la distance', 'sujet', 's', ha='left')
text(ax, 60, 31.5, 'au point 0 : 2² = 4', 'sujet', 's', ha='left')
save(fig, '56-052')
