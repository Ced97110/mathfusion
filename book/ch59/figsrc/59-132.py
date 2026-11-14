import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u, ox, oy = 11.0, 17.0, 8.0
P = lambda a, b: (ox + a * u, oy + b * u)
for a in range(5):
    for b in range(5):
        if (a, b) in [(0, 0), (1, 2), (2, 4)]:
            disc(ax, *P(a, b), 1.1, 'sujet')
        elif a == 0 and b in (1, 2):
            disc(ax, *P(a, b), 1.1, 'autre')
        else:
            disc(ax, *P(a, b), 0.7, 'fixe')
line(ax, [P(0, 0), P(2, 4)], 'sujet', dash=True)
arrow(ax, (P(0, 2)[0], P(0, 2)[1] + 3), (P(0, 4)[0], P(0, 4)[1] + 8), 'autre', lw=1.2)
text(ax, P(0, 4)[0] + 4, P(0, 4)[1] + 12, 'et ainsi de suite', 'autre', 's')
text(ax, P(2, 4)[0], P(2, 4)[1] + 4.5, '(2, 4)', 'sujet', 's')
text(ax, P(1, 2)[0] + 8, P(1, 2)[1] + 3, '(1, 2)', 'sujet', 's')
text(ax, P(0, 1)[0] - 2.5, P(0, 1)[1], '(0, 1)', 'autre', 's', ha='right')
text(ax, P(0, 2)[0] - 2.5, P(0, 2)[1], '(0, 2)', 'autre', 's', ha='right')
text(ax, 75, 62, 'déterminant', 'encre', 's')
text(ax, 75, 55, r'$2\times2-4\times1=0$', 'encre', 's')
text(ax, 75, 40, 'classes toutes', 'autre', 's')
text(ax, 75, 34, 'différentes :', 'autre', 's')
text(ax, 75, 24, 'déterminant 0', 'encre', 's', weight='bold')
text(ax, 75, 18, 'quotient infini', 'encre', 's', weight='bold')
save(fig, '59-132')
