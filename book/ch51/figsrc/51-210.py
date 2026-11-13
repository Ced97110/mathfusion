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

fig, ax = canvas(62)
cw = 7
text(ax, 44, 59, 'un seul 1 par tableau', 'sujet', 'm', weight='bold')
for i, ((r, c), lab) in enumerate([((0, 0), r'$e_{11}$'), ((0, 1), r'$e_{12}$'), ((1, 0), r'$e_{21}$'), ((1, 1), r'$e_{22}$')]):
    x = 5 + 22*i
    mat(ax, x, 38, cw, ones={(r, c): 'sujet'})
    text(ax, x + cw, 33, lab, 'sujet', 'm')
mat(ax, 8, 13, cw, ones={(0, 0): 'autre', (1, 1): 'autre'})
text(ax, 15, 7, 'tableau unité : deux 1', 'autre', 's')
mat(ax, 62, 13, cw)
text(ax, 69, 7, 'tableau nul : aucun 1', 'fixe', 's')
text(ax, 44, 20, 'case vide = 0', 'fixe', 's')
save(fig, '51-210')
