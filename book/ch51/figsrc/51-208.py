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

fig, ax = canvas(50)
cw = 11; y0 = 16
def blk(x, vals):
    for r in range(2):
        for c in range(2):
            hl = (r, c) == (0, 1)
            box(ax, x + c*cw, y0 + (1-r)*cw, cw, cw, 'varie' if hl else 'fixe', r=0.3, lw=0.7)
            text(ax, x + (c+.5)*cw, y0 + (1-r+.5)*cw, vals[r][c], 'varie' if hl else 'encre', 'm', weight='bold' if hl else 'normal')
blk(8, [['0', '−1'], ['2', '0']])
blk(58, [['0', '−2'], ['1', '0']])
text(ax, 19, y0 + 2*cw + 5, r'$RS$', 'sujet', 'l')
text(ax, 69, y0 + 2*cw + 5, r'$SR$', 'autre', 'l')
text(ax, 44, y0 + cw, '≠', 'limite', 'xl')
text(ax, 44, 8, 'case (1, 2) : −1 ≠ −2', 'varie', 'm')
save(fig, '51-208')
