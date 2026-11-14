import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
o = (38, 8); u = 9
P = iso(0, 0, 0, o, u); S = iso(4, 0, 0, o, u); O = iso(0, 3, 0, o, u); T = iso(0, 0, 3, o, u)
poly(ax, [P, S, O], 'sujet')
poly(ax, [P, S, T], 'varie', fill=False, lw=1.6); poly(ax, [P, O, T], 'varie', fill=False, lw=1.6)
for p, t, dx, dy in ((P, 'pied', 0, -4), (S, 'sud', 4, -2), (O, 'ouest', -5, -2), (T, 'sommet', 0, 4)):
    text(ax, p[0]+dx, p[1]+dy, t, 'encre', 's')
text(ax, 62, 50, 'triangle horizontal', 'sujet', 's', ha='center')
text(ax, 62, 44, '(sur la carte)', 'sujet', 's')
text(ax, 24, 56, '2 triangles verticaux', 'varie', 's')
save(fig, '27-123')
