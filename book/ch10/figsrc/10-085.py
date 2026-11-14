import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
k = 2.57
f = lambda v: 6 + (v - 36) * k
def row(y, title, pts, total, ends):
    text(ax, 4, y + 17, title, 'sujet', 'm', ha='left', weight='bold')
    line(ax, [(f(36), y), (f(64), y)], 'fixe')
    line(ax, [(f(50), y - 4), (f(50), y + 14)], 'varie', dash=True)
    text(ax, f(50), y - 6.5, '50', 'varie', 's')
    for v, h in pts:
        disc(ax, f(v), y, 1.6, 'sujet')
        arrow(ax, (f(v), y + h), (f(50) + (1 if v < 50 else -1), y + h), 'varie', lw=0.8)
        line(ax, [(f(v), y + 1.6), (f(v), y + h)], 'sujet', lw=0.5)
    text(ax, 44, y - 14, total, ends, 's')
row(60, 'A', [(38, 7), (41, 4), (59, 4), (62, 7)], 'estimée 200 = vraie 200', 'resultat')
for v, d in ((38, 0), (41, 0), (59, 0), (62, 0)): text(ax, f(v), 53.5, str(v), 'sujet', 's')
row(20, 'B', [(51, 4)], 'estimée 200, vraie 204', 'limite')
text(ax, f(51) + 2, 27.5, r'$4\times 51$', 'sujet', 's', ha='left')
save(fig, '10-085')
