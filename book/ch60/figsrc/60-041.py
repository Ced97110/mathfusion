import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx = lambda n: 16 + 13 * (n + 2)
cy = lambda h: 14 + 9 * h
text(ax, 44, 60, r'$M = \mathrm{tor}\,M \oplus L$', 'encre', 'l')
for n in range(-2, 3):
    for h in range(4):
        r = 'fixe'
        if n == 0: r = 'sujet'
        if h == 0: r = 'autre'
        if n == 0 and h == 0: r = 'resultat'
        disc(ax, cx(n), cy(h), 1.9, r)
box(ax, 9, 9, 66, 9, 'autre', fill=False, dash=True)
box(ax, cx(0) - 5.5, 9, 11, 36, 'sujet', fill=False, dash=True)
text(ax, cx(0), 49, 'tor M', 'sujet', 'm')
text(ax, 82, 14, 'L libre', 'autre', 's')
disc(ax, cx(2), cy(3), 2.4, 'varie')
line(ax, [(cx(2), cy(3) - 2.4), (cx(2), cy(0) + 2.1)], 'varie', lw=0.7, dash=True)
line(ax, [(cx(2) - 2.4, cy(3)), (cx(0) + 2.1, cy(3))], 'varie', lw=0.7, dash=True)
text(ax, 44, 3, '(2, 3) = (0, 3) + (2, 0)', 'varie', 's')
save(fig, '60-041')
