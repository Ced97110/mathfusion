import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def hasse(ax, y0, dy, roles=None, eroles=None):
    roles = roles or {}; eroles = eroles or {}
    P = {1: (44, y0), 2: (20, y0 + dy), 3: (44, y0 + dy), 5: (68, y0 + dy), 6: (20, y0 + 2 * dy),
         10: (44, y0 + 2 * dy), 15: (68, y0 + 2 * dy), 30: (44, y0 + 3 * dy)}
    E = [(1, 2), (1, 3), (1, 5), (2, 6), (3, 6), (2, 10), (5, 10), (3, 15), (5, 15), (6, 30), (10, 30), (15, 30)]
    t = 3.4 / dy
    for a, b in E:
        (x1, y1), (x2, y2) = P[a], P[b]
        p = (x1 + t * (x2 - x1), y1 + t * (y2 - y1)); q = (x2 - t * (x2 - x1), y2 - t * (y2 - y1))
        line(ax, [p, q], eroles.get((a, b), 'fixe'), lw=1.5 if (a, b) in eroles else 0.8)
    for n, (x, y) in P.items():
        box(ax, x - 5, y - 3, 10, 6, roles.get(n, 'fixe'), label=str(n))
    return P

fig, ax = canvas(92)
P = hasse(ax, 10, 22, roles={2: 'sujet', 3: 'sujet', 5: 'sujet'},
          eroles={(1, 2): 'sujet', (1, 3): 'sujet', (1, 5): 'sujet'})
text(ax, 80, 32, 'atomes', 'sujet', 'm')
text(ax, 44, 3, 'le plus petit', 'fixe', 's')
save(fig, '80-343')
