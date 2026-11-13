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

fig, ax = canvas(46)
cw, ch, x0 = 10, 9, 20
tops = [1, 2, 3, 4, 5]; res = [(2*k) % 6 for k in tops]
assert res == [2, 4, 0, 2, 4]
text(ax, 11, 32.5, r'$k$', 'fixe', 'm'); text(ax, 11, 18.5, r'$2\times k$', 'sujet', 'm')
for i, (k, v) in enumerate(zip(tops, res)):
    x = x0 + i*cw
    box(ax, x, 28, cw, ch, 'fixe', label=str(k), r=0.3, lw=0.7)
    box(ax, x, 14, cw, ch, 'sujet', label=str(v), r=0.3, lw=0.7)
    arrow(ax, (x + cw/2, 27.5), (x + cw/2, 23.5), 'varie')
box(ax, 74, 14, 10, 9, 'limite', fill=False, label='1', dash=True, r=0.3)
text(ax, 86, 9, 'jamais atteint', 'limite', 's', ha='right')
save(fig, '51-218')
