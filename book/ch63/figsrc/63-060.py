import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 18, 86, 'automorphisme', 'sujet', 's', weight='bold')
text(ax, 62, 86, 'symétrie du triangle', 'autre', 's', weight='bold')
names = ['1', r'$\sigma$', r'$\sigma^2$', r'$\tau$', r'$\sigma\tau$', r'$\sigma^2\tau$']
kinds = ['identité', '⅓ de tour', '⅔ de tour', 'miroir', 'miroir', 'miroir']
h = 3.46
for i in range(6):
    y = 74 - 12 * i
    box(ax, 4, y - 4.5, 24, 9, 'sujet', label=names[i])
    arrow(ax, (30, y), (36, y), 'fixe', both=True)
    top, bl, br = (48, y + h), (44, y - h), (52, y - h)
    poly(ax, [top, bl, br], 'autre')
    gx, gy = 48, y - h / 3
    if i in (1, 2):
        span = 120 if i == 1 else 240
        pts = [(gx + 2.0 * math.cos(math.radians(60 + span * t / 10)), gy + 2.0 * math.sin(math.radians(60 + span * t / 10))) for t in range(11)]
        line(ax, pts, 'varie', lw=1.0)
        arrow(ax, pts[-2], pts[-1], 'varie', lw=1.0)
    if i >= 3:
        v = [top, bl, br][i - 3]
        mid = [((bl[0] + br[0]) / 2, bl[1]), ((top[0] + br[0]) / 2, (top[1] + br[1]) / 2), ((top[0] + bl[0]) / 2, (top[1] + bl[1]) / 2)][i - 3]
        dx, dy = mid[0] - v[0], mid[1] - v[1]
        n = math.hypot(dx, dy)
        ux, uy = dx / n, dy / n
        line(ax, [(v[0] - 1.8 * ux, v[1] - 1.8 * uy), (mid[0] + 1.8 * ux, mid[1] + 1.8 * uy)], 'resultat', lw=1.0, dash=True)
    text(ax, 72, y, kinds[i], 'encre', 'm')
save(fig, '63-060')
