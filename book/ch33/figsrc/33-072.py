import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
ox, oy, S = 44, 44, 17.0; h = math.pi / 2
ts = [-h + i * math.pi / 80 for i in range(81)]
line(ax, [(ox - 30, oy), (ox + 30, oy)], 'fixe', lw=0.5); line(ax, [(ox, oy - 30), (ox, oy + 30)], 'fixe', lw=0.5)
line(ax, [(ox - 29, oy - 29), (ox + 29, oy + 29)], 'fixe', lw=1.0, dash=True)
line(ax, [(ox + t * S, oy + math.sin(t) * S) for t in ts], 'sujet', lw=1.8)
line(ax, [(ox + math.sin(t) * S, oy + t * S) for t in ts], 'varie', lw=1.8)
for t in (-1.2, -0.7, 0.2, 1.1):
    p = (ox + t * S, oy + math.sin(t) * S); q = (ox + math.sin(t) * S, oy + t * S)
    arrow(ax, p, q, 'resultat', lw=0.8)
    disc(ax, *p, 0.9, 'sujet'); disc(ax, *q, 0.9, 'varie')
a = math.pi / 6; p = (ox + a * S, oy + 0.5 * S); q = (ox + 0.5 * S, oy + a * S)
arrow(ax, p, q, 'resultat', lw=1.2); disc(ax, *p, 1.4, 'sujet'); disc(ax, *q, 1.4, 'varie')
text(ax, ox + 26, oy + 3, r'$(\pi/6,\ 0{,}5)$', 'sujet', 's')
line(ax, [(ox + 19, oy + 4.5), p], 'sujet', lw=0.5)
text(ax, ox - 7, oy + 19, r'$(0{,}5,\ \pi/6)$', 'varie', 's', ha='right')
line(ax, [(ox - 6, oy + 18), q], 'varie', lw=0.5)
text(ax, ox + 22, oy - 12, 'sinus restreint', 'sujet', 'm'); text(ax, ox - 14, oy + 27, 'arcsinus', 'varie', 'm')
text(ax, ox + 33, oy + 34, r'$y=x$', 'fixe', 'm')
save(fig, '33-072')
