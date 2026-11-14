import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, cw, ones=None, tint=None, base='fixe', show=True, allrole=None):
    ones = ones or {}; tint = tint or {}
    for r in range(2):
        for c in range(2):
            role = ones.get((r, c), tint.get((r, c), allrole or base))
            box(ax, x + c*cw, y + (1-r)*cw, cw, cw, role, r=0.3, lw=0.7)
            if (r, c) in ones and show:
                text(ax, x + (c+.5)*cw, y + (1-r+.5)*cw, '1', ones[(r, c)], 'm', weight='bold')

def dial(ax, cx, cy, R, n, roles=None, rd=1.5):
    roles = roles or {}
    disc(ax, cx, cy, R, 'fixe', fill=False)
    pts = []
    for k in range(n):
        a = math.radians(90 - 360*k/n); p = (cx + R*math.cos(a), cy + R*math.sin(a)); pts.append(p)
        disc(ax, p[0], p[1], rd, roles.get(k, 'sujet'))
    return pts

fig, ax = canvas(56)
x0, w = 14, 10
assert [(a*b) % 7 for a, b in [(1, 1), (2, 4), (3, 5), (6, 6)]] == [1, 1, 1, 1]
text(ax, 44, 51, r'$\mathbb{Z}/\,7$ : inverses', 'sujet', 'l', weight='bold')
cx = lambda v: x0 + (v - 0.5)*w
for v in range(1, 7): box(ax, x0 + (v-1)*w, 22, w, 10, 'sujet', label=str(v), r=0.3, lw=0.7)
arrow(ax, (cx(2), 33), (cx(4), 33), 'resultat', curve=-0.5, both=True)
text(ax, cx(3), 41, '2 × 4 = 1', 'resultat', 'm')
arrow(ax, (cx(3), 21), (cx(5), 21), 'resultat', curve=0.5, both=True)
text(ax, cx(4), 11, '3 × 5 = 1', 'resultat', 'm')
for v in (1, 6):
    line(ax, [(cx(v), 32), (cx(v), 36)], 'resultat')
    text(ax, cx(v), 39, f'{v} × {v} = 1', 'resultat', 'm')
save(fig, '51-220')
