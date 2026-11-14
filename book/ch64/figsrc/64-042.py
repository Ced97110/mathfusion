import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
w = 14; h = 12
xs = [2, 25.3, 48.7, 72]
yt, yb = 58, 12
Z = r'$\mathbb{Z}/60$'
# deux cases tall (début et fin communs aux deux suites)
box(ax, xs[0], yb, w, yt + h - yb, 'fixe', label=Z + '\n60', size='s')
box(ax, xs[3], yb, w, yt + h - yb, 'fixe', label=r'$\{0\}$' + '\n1', size='s')
tops = [r'$\langle3\rangle$' + '\n20', r'$\langle15\rangle$' + '\n4']
bots = [r'$\langle4\rangle$' + '\n15', r'$\langle20\rangle$' + '\n3']
for i in (1, 2):
    box(ax, xs[i], yt, w, h, 'sujet', label=tops[i - 1], size='s')
    box(ax, xs[i], yb, w, h, 'autre', label=bots[i - 1], size='s')
for i in range(3):
    arrow(ax, (xs[i] + w + 0.3, yt + h / 2), (xs[i + 1] - 0.3, yt + h / 2), 'sujet')
    arrow(ax, (xs[i] + w + 0.3, yb + h / 2), (xs[i + 1] - 0.3, yb + h / 2), 'autre')
gx = [xs[i] + w + (xs[i + 1] - xs[i] - w) / 2 for i in range(3)]
rd = 2.8
ty, by = yt - 5.2, yb + h + 5.2
topf = {'3': gx[0], '5': gx[1], '4': gx[2]}
botf = {'4': gx[0], '5': gx[1], '3': gx[2]}
role = {'3': 'varie', '4': 'autre', '5': 'resultat'}
def bez(p, q, bend):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); nx, ny = -(q[1] - p[1]) / d, (q[0] - p[0]) / d
    c = ((p[0] + q[0]) / 2 + nx * bend, (p[1] + q[1]) / 2 + ny * bend)
    return [((1 - t) ** 2 * p[0] + 2 * t * (1 - t) * c[0] + t * t * q[0],
             (1 - t) ** 2 * p[1] + 2 * t * (1 - t) * c[1] + t * t * q[1]) for t in [i / 24 for i in range(25)]]
for k in ('3', '4', '5'):
    p = (topf[k], ty); q = (botf[k], by)
    pts = bez(p, q, 0 if k == '5' else 9)
    pts = [a for a in pts if math.hypot(a[0] - p[0], a[1] - p[1]) > rd and math.hypot(a[0] - q[0], a[1] - q[1]) > rd]
    line(ax, pts, role[k], lw=1.4)
for k in ('3', '4', '5'):
    disc(ax, topf[k], ty, rd, role[k], label=k, size='m')
    disc(ax, botf[k], by, rd, role[k], label=k, size='m')
text(ax, 44, 3.5, 'mêmes facteurs, autre ordre', 'resultat', 's', weight='bold')
save(fig, '64-042')
