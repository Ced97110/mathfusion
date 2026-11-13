import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, y0, d = 22, 14, 13
P = lambda m, n: (x0 + d * m, y0 + d * n)
text(ax, x0 - 9, P(0, 3)[1] + 7, r'$m+n$', 'fixe', 's')
for dd in range(4):
    cells = [(m, dd - m) for m in range(dd + 1)]
    if dd: line(ax, [P(*c) for c in cells], 'fixe', lw=0.8)
    for c in cells:
        disc(ax, *P(*c), 2.4, 'varie' if c == (2, 1) else 'sujet')
    text(ax, P(0, dd)[0] - 6, P(0, dd)[1], str(dd), 'fixe', 'm')
    text(ax, P(dd, 0)[0], y0 - 6, f'{dd + 1} point' + ('s' if dd else ''), 'sujet', 's')
text(ax, P(2, 1)[0] + 2, P(2, 1)[1] + 5, '(2, 1)', 'varie', 's', ha='left')
text(ax, 71, 52, r'$1+2+3+4$', 'sujet', 'm')
text(ax, 71, 42, r'$=10$ points', 'resultat', 'm')
text(ax, 71, 32, r'$4\times5/2=10$', 'resultat', 'm')
save(fig, '43-121')
