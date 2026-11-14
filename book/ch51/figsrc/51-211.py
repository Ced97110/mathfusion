import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, cw, ones=None, tint=None, base='fixe', show=True, allrole=None):
    ones = ones or {}; tint = tint or {}
    for r in range(2):
        for c in range(2):
            role = ones.get((r, c), tint.get((r, c), allrole or base))
            box(ax, x + c*cw, y + (1-r)*cw, cw, cw, role, r=0.3, lw=0.7)
            if (r, c) in ones and show:
                text(ax, x + (c+.5)*cw, y + (1-r+.5)*cw, '1', ones[(r, c)], 'm', weight='bold')
            elif show:
                text(ax, x + (c+.5)*cw, y + (1-r+.5)*cw, '0', 'fixe', 'm')

def dial(ax, cx, cy, R, n, roles=None, rd=1.5):
    roles = roles or {}
    disc(ax, cx, cy, R, 'fixe', fill=False)
    pts = []
    for k in range(n):
        a = math.radians(90 - 360*k/n); p = (cx + R*math.cos(a), cy + R*math.sin(a)); pts.append(p)
        disc(ax, p[0], p[1], rd, roles.get(k, 'sujet'))
    return pts

fig, ax = canvas(58)
cw = 13; gx, gy = 52, 20
text(ax, 22, 44.5, r'$e_{ij}$', 'sujet', 'xl')
text(ax, 22, 26, r'$e$ : nom du tableau', 'sujet', 'm')
text(ax, 22, 18, r'$i$ : numéro de ligne', 'varie', 'm')
text(ax, 22, 10, r'$j$ : numéro de colonne', 'autre', 'm')
mat(ax, gx, gy, cw, ones={(0, 1): 'sujet'}, tint={(0, 0): 'varie', (1, 1): 'autre'})
text(ax, gx - 3.5, gy + 1.5*cw, 'ligne 1', 'varie', 's', ha='right')
text(ax, gx + 1.5*cw, gy + 2*cw + 3.5, 'colonne 2', 'autre', 's')
for bx, d in ((gx - 1.5, 1.2), (gx + 2*cw + 1.5, -1.2)):
    line(ax, [(bx + d, gy - 1.5), (bx, gy - 1.5), (bx, gy + 2*cw + 1.5), (bx + d, gy + 2*cw + 1.5)], 'sujet', lw=1.0)
text(ax, gx + cw, gy - 5, r'$e_{12}$ : tout ce tableau', 'sujet', 'm')
arrow(ax, (31, 44.5), (46.5, 44.5), 'sujet', lw=1.0)
text(ax, 39, 48.5, r'$i=1,\ j=2$', 'sujet', 's')
save(fig, '51-211')
