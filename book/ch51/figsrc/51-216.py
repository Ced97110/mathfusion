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

fig, ax = canvas(72)
R = 12
for cx, n, role, titre, eq, why, verdict, hi in [
        (22, 7, 'resultat', r'$\mathbb{Z}/\,7$', '3 × 5 = 1', '7 est premier', 'corps', 1),
        (66, 6, 'limite', r'$\mathbb{Z}/\,6$', '2 × 3 = 0', r'6 = 2 × 3', 'pas un corps', 0)]:
    text(ax, cx, 67, titre, 'sujet', 'l', weight='bold')
    pts = dial(ax, cx, 42, R, n, roles={hi: role})
    def lab(k, s, r_):
        a = math.radians(90 - 360*k/n)
        text(ax, cx + (R + 4)*math.cos(a), 42 + (R + 4)*math.sin(a), s, r_, 'm', weight='bold')
    lab(hi, str(hi), role)
    if n == 7: lab(0, '0', 'fixe')
    text(ax, cx, 23, eq, role, 'm', weight='bold')
    text(ax, cx, 16.5, why, 'fixe', 'm')
    text(ax, cx, 8, verdict, role, 'l', weight='bold')
save(fig, '51-216')
