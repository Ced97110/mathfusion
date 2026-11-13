import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
ox, oy, u = 4, 6, 11
m = lambda x, y: (ox + (x + 1) * u, oy + (y + 1) * u)
poly(ax, [m(-1, -1), m(4, -1), m(4, 4), m(-1, 4)], 'fixe', fill=False)
line(ax, [m(-1, 0), m(4, 0)], 'fixe'); line(ax, [m(0, -1), m(0, 4)], 'fixe')
poly(ax, [m(-1, -1), m(-1, 0), m(1, 2), m(4, -1)], 'resultat')
line(ax, [m(-1, 0), m(3, 4)], 'varie', lw=1.3)
line(ax, [m(-1, 4), m(4, -1)], 'sujet', lw=1.3)
S = m(1, 2); disc(ax, S[0], S[1], 1.5, 'resultat')
text(ax, S[0] + 2.8, S[1], r'$S=(1,\,2)$', 'resultat', 's', ha='left', weight='bold')
text(ax, S[0], S[1] + 7, 'sommet', 'resultat', 's')
rows = [('varie', 'frontière 1'), ('sujet', 'frontière 2'), ('resultat', 'zone')]
for i, (r, t) in enumerate(rows):
    y = 52 - i * 12
    if r == 'resultat': poly(ax, [(62, y - 1.5), (66, y - 1.5), (66, y + 1.5), (62, y + 1.5)], r)
    else: line(ax, [(62, y), (66, y)], r, lw=1.3)
    text(ax, 68, y, t, r, 's', ha='left')
save(fig, '20-101')
