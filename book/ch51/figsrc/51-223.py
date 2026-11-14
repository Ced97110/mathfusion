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

fig, ax = canvas(70)
rows = [(50, 'prémisse 1', 'sujet', 'D est intègre', r'$\mathbb{Z}/\,7$ : aucun diviseur de 0'),
        (32, 'prémisse 2', 'sujet', 'D est fini', r'$\mathbb{Z}/\,7$ : 7 éléments'),
        (6, 'conclusion', 'resultat', 'tout non nul a un inverse', r'$\mathbb{Z}/\,7$ : 3 × 5 = 1')]
for y, lab, role, main, case in rows:
    text(ax, 13, y + 7, lab, role, 'm')
    box(ax, 26, y, 59, 14, role)
    text(ax, 55.5, y + 9.5, main, role, 'm', weight='bold')
    text(ax, 55.5, y + 4, case, 'fixe', 's')
line(ax, [(26, 28), (85, 28)], 'encre', lw=1.3)
text(ax, 13, 28, 'donc', 'varie', 'm', weight='bold')
save(fig, '51-223')
