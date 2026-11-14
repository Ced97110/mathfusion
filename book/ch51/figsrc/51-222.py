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

fig, ax = canvas(50)
w = 11; x0 = 11
tops = [1, 2, 3, 4, 5, 6]; res = [(3*k) % 7 for k in tops]
assert res == [3, 6, 2, 5, 1, 4] and sorted(res) == tops
text(ax, 5.5, 32, '× 3', 'varie', 'm', weight='bold')
for i, (k, v) in enumerate(zip(tops, res)):
    x = x0 + i*w
    box(ax, x, 36, w, 10, 'resultat' if k == 5 else 'fixe', label=str(k), r=0.3, lw=0.7)
    box(ax, x, 18, w, 10, 'resultat' if v == 1 else 'sujet', label=str(v), r=0.3, lw=0.7)
    arrow(ax, (x + w/2, 35.5), (x + w/2, 28.5), 'varie')
text(ax, 44, 11, 'tous différents : 1 atteint', 'resultat', 'm', weight='bold')
save(fig, '51-222')
