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

fig, ax = canvas(68)
text(ax, 44, 64, r'$\mathbb{Q}$, $\mathbb{R}$ : infinis', 'fixe', 'm', weight='bold')
arrow(ax, (6, 57), (82, 57), 'fixe', both=True)
for i in range(9): disc(ax, 14 + 7.5*i, 57, 1.1, 'fixe')
text(ax, 44, 42, 'corps finis : on y divise', 'sujet', 'm', weight='bold')
for cx, n in zip([11, 33, 55, 77], [2, 3, 5, 7]):
    dial(ax, cx, 24, 7, n)
    text(ax, cx, 36, rf'$\mathbb{{Z}}/\,{n}$', 'sujet', 'm')
    text(ax, cx, 11, f'{n} éléments', 'sujet', 's')
save(fig, '51-221')
