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

fig, ax = canvas(78)
line(ax, [(41, 28), (41, 76)], 'fixe', lw=0.6); line(ax, [(3, 27), (85, 27)], 'fixe', lw=0.6)
text(ax, 21, 72, 'taille 1', 'sujet', 'l', weight='bold')
box(ax, 9, 54, 24, 8, 'resultat', label='2 × 3 = 6'); box(ax, 9, 42, 24, 8, 'resultat', label='3 × 2 = 6')
text(ax, 21, 33, 'égaux', 'resultat', 'm')
text(ax, 64, 72, 'taille 2', 'sujet', 'l', weight='bold')
cw = 4.5
for y, A, Bm, C in [(52, {(0, 0): 'sujet'}, {(0, 1): 'sujet'}, {(0, 1): 'resultat'}), (38, {(0, 1): 'sujet'}, {(0, 0): 'sujet'}, {})]:
    mat(ax, 45, y, cw, ones=A); mat(ax, 60, y, cw, ones=Bm); mat(ax, 75, y, cw, ones=C, show=False)
    text(ax, 57.5, y + cw, '×', 'encre', 'l'); text(ax, 72.5, y + cw, '=', 'encre', 'l')
text(ax, 64, 33, 'différents', 'limite', 'm')
mat(ax, 6, 6, cw, show=False)
text(ax, 19, 13, r'$R=\{0\}$', 'sujet', 'm', ha='left')
text(ax, 19, 7.5, 'un seul tableau : le nul', 'fixe', 's', ha='left')
text(ax, 66, 8, 'bleu : un 1', 'sujet', 's')
save(fig, '51-214')
