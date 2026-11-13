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

fig, ax = canvas(76)
s = 4.6; x0 = 6
text(ax, 44, 72, r'départ : $n$ = 7, $a$ = 3', 'sujet', 'm', weight='bold')
for i in range(5): box(ax, x0 + 3*s*i, 50, 3*s, 8, 'sujet', r=0.3, lw=0.7)
text(ax, x0 + 7.5*s, 62, '5 × 3 = 15', 'sujet', 'm')
for i in range(2): box(ax, x0 + 7*s*i, 36, 7*s, 8, 'autre', r=0.3, lw=0.7)
box(ax, x0 + 14*s, 36, s, 8, 'varie', r=0.3, lw=0.7)
text(ax, x0 + 7*s, 31.5, '2 × 7 = 14', 'autre', 'm')
text(ax, x0 + 14.5*s, 31.5, '1', 'varie', 'm', weight='bold')
line(ax, [(x0 + 14*s, 44), (x0 + 14*s, 50)], 'varie', dash=True)
text(ax, 44, 24, r'étape : $u\,a+v\,n=1$', 'varie', 'm', weight='bold')
text(ax, 44, 18, '5 × 3 − 2 × 7 = 15 − 14 = 1', 'varie', 'm')
text(ax, 44, 9, 'sur le cadran, 2 × 7 = 0', 'resultat', 'm')
text(ax, 44, 3.5, r'donc 5 × 3 = 1 : $u$ = 5', 'resultat', 'm', weight='bold')
save(fig, '51-219')
