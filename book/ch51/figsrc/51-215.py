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
cw = 9; gy = 22
xs = [4, 32, 60]
mat(ax, xs[0], gy, cw, ones={(0, 1): 'sujet'}, tint={(1, 1): 'varie'})
mat(ax, xs[1], gy, cw, ones={(0, 0): 'sujet'}, tint={(1, 0): 'varie', (1, 1): 'varie'})
mat(ax, xs[2], gy, cw, allrole='resultat')
text(ax, 27, gy + cw, '×', 'encre', 'xl'); text(ax, 55, gy + cw, '=', 'encre', 'xl')
for x, lab, role in zip(xs, [r'$e_{12}$', r'$e_{11}$', r'$0$'], ['sujet', 'sujet', 'resultat']):
    text(ax, x + cw, gy - 4, lab, role, 'm')
text(ax, xs[0] + cw, 12, 'non nul', 'sujet', 's'); text(ax, xs[1] + cw, 12, 'non nul', 'sujet', 's')
text(ax, xs[2] + cw, 12, 'nul', 'resultat', 's')
text(ax, 44, 48, 'orange : le 1 lit que des 0', 'varie', 's')
text(ax, 44, 4.5, 'deux non nuls, produit nul', 'limite', 'm', weight='bold')
save(fig, '51-215')
