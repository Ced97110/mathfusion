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

fig, ax = canvas(64)
s = 13; O = (30, 14)
P = lambda x, y: (O[0] + s*x, O[1] + s*y)
line(ax, [P(-1.3, 0), P(3.4, 0)], 'fixe', lw=0.5)
line(ax, [P(0, 0), P(0, 3.4)], 'fixe', lw=0.5)
u, Su, RSu = (1.5, 0.5), (3, 0.5), (-0.5, 3)
Ru, SRu = (-0.5, 1.5), (-1, 1.5)
arrow(ax, P(0, 0), P(*u), 'sujet')
arrow(ax, P(*u), P(*Su), 'varie'); arrow(ax, P(*Su), P(*RSu), 'varie')
arrow(ax, P(*u), P(*Ru), 'autre'); arrow(ax, P(*Ru), P(*SRu), 'autre')
for pt, role in [(u, 'sujet'), (Su, 'varie'), (RSu, 'varie'), (Ru, 'autre'), (SRu, 'autre')]:
    disc(ax, *P(*pt), 1.1, role)
text(ax, P(1.5, 0.5)[0], P(1.5, 0.5)[1] + 4, r'$u$', 'sujet')
text(ax, P(3, 0.5)[0] + 3, P(3, 0.5)[1], r'$Su$', 'varie', ha='left')
text(ax, P(-0.5, 1.5)[0], P(-0.5, 1.5)[1] + 4, r'$Ru$', 'autre')
text(ax, P(-0.5, 3)[0], P(-0.5, 3)[1] + 4.5, r'$RSu$ (−0,5 ; 3)', 'varie')
text(ax, P(-1, 1.5)[0], P(-1, 1.5)[1] - 4, r'$SRu$ (−1 ; 1,5)', 'autre')
arrow(ax, (47, 53), (55, 53), 'varie'); text(ax, 57, 53, 'étirer puis tourner', 'varie', 's', ha='left')
arrow(ax, (47, 46), (55, 46), 'autre'); text(ax, 57, 46, 'tourner puis étirer', 'autre', 's', ha='left')
save(fig, '51-209')
