import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, ch, x0, yt = 12, 11, 10, 46
ctr = lambda i, j: (x0 + (j + 0.5) * cw, yt - (i + 0.5) * ch)
steps = {(1, 1): '1', (0, 2): '2', (1, 3): '3', (0, 4): '4', (1, 5): '5', (0, 0): '0 et 6'}
for i in range(2):
    for j in range(6):
        lab = steps.get((i, j))
        role = 'resultat' if (i, j) == (0, 0) else 'sujet' if lab else 'fixe'
        box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, role, label=None, size='s', r=0.6)
for i in range(2): text(ax, x0 - 3.5, ctr(i, 0)[1], str(i), 'fixe', 's')
for j in range(6): text(ax, ctr(0, j)[0], yt + 3, str(j), 'fixe', 's')
path = [(0, 0), (1, 1), (0, 2), (1, 3), (0, 4), (1, 5)]
def cut(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    return (p[0] + u[0] * r, p[1] + u[1] * r), (q[0] - u[0] * r, q[1] - u[1] * r)
for a, b in zip(path[:-1], path[1:]):
    p, q = cut(ctr(*a), ctr(*b), 4.2)
    arrow(ax, p, q, 'varie', lw=0.9)
    text(ax, (p[0]+q[0])/2 + 2.6, (p[1]+q[1])/2, str(path.index(b)), 'varie', 's', weight='bold')
yb = yt - 2 * ch - 3.5; xl = x0 - 7; yin = ctr(0, 0)[1] + 3.5
line(ax, [(ctr(1, 5)[0], yt - 2 * ch), (ctr(1, 5)[0], yb), (xl, yb), (xl, yin)], 'varie', lw=0.9)
arrow(ax, (xl, yin), (x0 + 0.2, yin), 'varie', lw=0.9)
text(ax, (xl + ctr(1, 5)[0]) / 2, yb - 2.6, '6', 'varie', 's', weight='bold')
text(ax, 44, 3, '+ (1, 1), six fois de suite', 'varie', 's')
save(fig, '60-008')
