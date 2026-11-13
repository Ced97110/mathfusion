import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
x0, y0, d = 30, 10, 13
P = lambda m, n: (x0 + d * m, y0 + d * n)
for m in range(4):
    for n in range(4):
        if m + n > 3: disc(ax, *P(m, n), 1.4, 'fixe')
for dd in range(4):
    cells = [(m, dd - m) for m in range(dd + 1)]
    if dd: line(ax, [P(*c) for c in cells], 'sujet', lw=1.0)
    for c in cells: disc(ax, *P(*c), 2.4, 'sujet')
    text(ax, P(0, dd)[0] - 5, P(0, dd)[1], r'$m+n=%d$' % dd, 'sujet', 's', ha='right')
text(ax, x0 + 2 * d, y0 - 7, r'$m$ : abscisse', 'fixe', 's')
text(ax, 4, 60, r'$n$ : ordonnée', 'fixe', 's', ha='left')
text(ax, 74, 52, r'puis $m+n=4$…', 'varie', 's')
save(fig, '43-119')
