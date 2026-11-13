import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
k = 4.8
def panel(ox, sacs, ok, cap, verdict):
    oy = 14
    P = lambda a, b: (ox + a * k, oy + b * k)
    for i in range(0, 6): line(ax, [P(i, 0), P(i, 5)], 'fixe', lw=0.2)
    for j in range(0, 6): line(ax, [P(0, j), P(5.4, j)], 'fixe', lw=0.2)
    if not ok:
        line(ax, [P(0, 0), P(5.4, 0)], 'sujet', lw=2.0)
        text(ax, P(2.7, 0)[0], P(0, 1.1)[1], 'seulement cette droite', 'sujet', 's')
    for (a, b) in sorted(sacs, key=lambda s: -s[0]):
        arrow(ax, P(0, 0), P(a, b), 'sujet', lw=1.2 + 0.8 * (a == 1 and b == 0 and len(sacs) == 3))
    col = 'resultat' if ok else 'limite'
    disc(ax, *P(5, 4), 1.3, col)
    text(ax, P(4.7, 4)[0], P(4.7, 4)[1], '(5, 4)', col, 's', ha='right')
    text(ax, ox + 12, 46, verdict, col, 's')
    text(ax, ox + 12, 6, cap, 'sujet', 's')
panel(2, [(1, 0), (0, 1)], True, '(1, 0), (0, 1)', 'engendrent')
panel(31, [(1, 0), (2, 0), (0, 1)], True, '(1, 0), (2, 0),\n(0, 1)', 'engendrent')
panel(60, [(1, 0)], False, '(1, 0)', 'n’engendre pas')
save(fig, '58-043')
