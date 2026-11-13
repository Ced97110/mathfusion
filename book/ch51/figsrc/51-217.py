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

fig, ax = canvas(58)
cs = [14, 44, 74]; roles = ['sujet', 'varie', 'resultat']
heads = ['départ', 'étape décisive', 'arrivée']
for c, role, h in zip(cs, roles, heads):
    box(ax, c - 12.5, 4, 25, 50, role, fill=True, lw=0.9)
    text(ax, c, 49.5, h, role, 'm', weight='bold')
arrow(ax, (26.7, 29), (31.3, 29), 'fixe'); arrow(ax, (56.7, 29), (61.3, 29), 'fixe')
for i in range(6): disc(ax, cs[0] - 9 + 3.6*i, 38, 1.4, 'sujet')
text(ax, cs[0], 29, r'$n$ = 6', 'sujet', 'm'); text(ax, cs[0], 21, 'pas premier', 'sujet', 'm')
for i in range(2):
    for j in range(3): disc(ax, cs[1] - 4.2 + 4.2*j, 41 - 4.2*i, 1.4, 'varie')
text(ax, cs[1], 29, '6 = 2 × 3', 'varie', 'm', weight='bold')
text(ax, cs[1], 21, r'$a$ = 2 ; $b$ = 3', 'varie', 'm')
text(ax, cs[2], 41, 'sur le cadran :', 'resultat', 's')
text(ax, cs[2], 34, '2 × 3 = 0', 'resultat', 'l', weight='bold')
text(ax, cs[2], 26, '2 ≠ 0 et 3 ≠ 0', 'resultat', 's')
text(ax, cs[2], 18, 'pas un corps', 'resultat', 'm', weight='bold')
save(fig, '51-217')
