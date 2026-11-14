import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy, R = 44, 42, 24
t = math.radians(120); P = (ox + R * math.cos(t), oy + R * math.sin(t)); Hh = (P[0], oy)
q = [(ox, oy)] + [(ox + R * math.cos(math.radians(a)), oy + R * math.sin(math.radians(a))) for a in range(0, 91, 5)]
poly(ax, q, 'fixe')
disc(ax, ox, oy, R, 'fixe', fill=False)
line(ax, [(ox - 26, oy), (ox + 26, oy)], 'fixe'); line(ax, [(ox, oy - 26), (ox, oy + 26)], 'fixe')
poly(ax, [(ox, oy), Hh, P], 'sujet')
line(ax, [(ox, oy), Hh], 'autre', lw=1.6); line(ax, [Hh, P], 'varie', lw=1.6); line(ax, [(ox, oy), P], 'sujet', lw=1.6)
text(ax, ox + 13, oy + 11, '1er quart', 'fixe', 's')
text(ax, P[0], P[1] + 3, '$P$', 'sujet', 's'); text(ax, Hh[0], oy - 3, '$H$', 'encre', 's'); text(ax, ox + 2.5, oy - 3, '$O$', 'encre', 's')
text(ax, (ox + Hh[0]) / 2, oy + 2.8, '0,5', 'autre', 's'); text(ax, Hh[0] - 5.5, oy + 10.4, '0,8660', 'varie', 's')
text(ax, ox + 20, oy + 23, r'$\theta=120^\circ$', 'fixe', 's')
text(ax, 44, 14, r'$\cos\theta=-0{,}5$ : carré 0,25', 'autre', 's')
text(ax, 44, 8.5, r'$\sin\theta=0{,}8660$ : carré 0,75', 'varie', 's')
text(ax, 44, 3.2, '0,25 + 0,75 = 1', 'resultat', 's', weight='bold')
save(fig, '31-069')
