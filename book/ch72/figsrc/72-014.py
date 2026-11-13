import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)

fig, ax = canvas(70)
rows = [(r'départ : $y$ = (1, 2)', 'autre'),
        (r'1. $p$ = (1,6 ; 0,8)', 'resultat'),
        (r'2. $q = y - p$ = ($-$0,6 ; 1,2)', 'varie'),
        (r'3. contrôle : $B(q,x)$ = 0', 'resultat')]
for k, (l, r) in enumerate(rows):
    y = 56 - k * 16
    box(ax, 2, y, 46, 11, r, label=l, size='s')
    if k: arrow(ax, (25, y + 16 - 0.6), (25, y + 11.6), 'fixe', lw=0.8)
ox, oy, u = 54, 12, 12
P = lambda x, y: (ox + x * u, oy + y * u)
axes(ax, ox, oy, u, -0.8, 1.9, -0.2, 2.5)
arrow(ax, P(0, 0), P(2, 1), 'sujet', lw=1.2)
arrow(ax, P(0, 0), P(1, 2), 'autre', lw=1.2)
arrow(ax, P(0, 0), P(1.6, 0.8), 'resultat', lw=2.2)
arrow(ax, P(1.6, 0.8), P(1, 2), 'varie', lw=1.5)
# right-angle mark between q and x at the tip of p
d1 = (2 / 5 ** .5, 1 / 5 ** .5); d2 = (-1 / 5 ** .5, 2 / 5 ** .5); k = 2.6
t = P(1.6, 0.8)
a = (t[0] - k * d1[0], t[1] - k * d1[1]); b = (a[0] + k * d2[0], a[1] + k * d2[1]); c = (t[0] + k * d2[0], t[1] + k * d2[1])
line(ax, [a, b, c], 'resultat', lw=0.8)
text(ax, P(2, 1)[0] + 5, P(2, 1)[1] + 4, r'$x$ = (2, 1)', 'sujet', 's', ha='right')
text(ax, P(1, 2)[0] - 2.5, P(1, 2)[1] + 3, r'$y$', 'autre', 'm')
text(ax, P(1.6, 0.8)[0] - 2, P(1.6, 0.8)[1] - 4, r'$p$', 'resultat', 'm')
text(ax, P(1.3, 1.4)[0] - 4, P(1.3, 1.4)[1] + 1, r'$q$', 'varie', 'm')
save(fig, '72-014')
