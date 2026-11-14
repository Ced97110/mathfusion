import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(56)
line(ax, [(4, 12), (86, 12)], 'fixe', lw=0.8)
for x, sh, th, ttl, rap, ang, ax_, ay_, rr in [(10, 8, 63.435, 'midi', 'rapport 2', 'angle grand', 30, 24, 5), (44, 32, 26.565, 'soir', 'rapport 0,5', 'angle petit', 68, 26, 9)]:
    line(ax, [(x, 12), (x, 28)], 'fixe', lw=2.0)
    line(ax, [(x, 12), (x + sh, 12)], 'sujet', lw=2.2)
    line(ax, [(x, 28), (x + sh, 12)], 'encre', dash=True, lw=0.8)
    arc(ax, (x + sh, 12), rr, 180 - th, 180, 'varie', 1.2)
    text(ax, x + 4 if x < 20 else x + 16, 50, ttl, 'encre', 'm', weight='bold')
    text(ax, x + 4 if x < 20 else x + 16, 44, rap, 'resultat', 'm')
    text(ax, x, 34, 'bâton 2 m', 'fixe', 's')
    text(ax, x + sh / 2, 6.5, 'ombre %s m' % ('1' if sh == 8 else '4'), 'sujet', 's')
    text(ax, ax_, ay_, ang, 'varie', 's')
save(fig, '25-010')
