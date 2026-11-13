import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
x0, y0, d = 26, 10, 12
P = lambda m, n: (x0 + d * m, y0 + d * n)
for m in range(5):
    for n in range(5):
        if m + n not in (3, 4): disc(ax, *P(m, n), 1.3, 'fixe')
line(ax, [P(m, 4 - m) for m in range(5)], 'fixe', lw=0.8, dash=True)
for m in range(5): disc(ax, *P(m, 4 - m), 2.0, 'fixe', fill=False)
line(ax, [P(m, 3 - m) for m in range(4)], 'sujet', lw=1.0)
for m in range(4):
    disc(ax, *P(m, 3 - m), 2.4, 'sujet')
    x, y = P(m, 3 - m)
    text(ax, x - 1.2, y - 3.8, f'({m}, {3 - m})', 'sujet', 's', ha='right')
text(ax, P(0, 4)[0] - 4, P(0, 4)[1] + 1, r'$d=4$ : 5 points', 'fixe', 's', ha='right')
text(ax, P(0, 3)[0] - 4, P(0, 3)[1] + 4.5, r'$d=3$ : 4 points', 'sujet', 's', ha='right')
text(ax, 70, 68, r'$d+1$ points', 'resultat', 'm')
save(fig, '43-120')
