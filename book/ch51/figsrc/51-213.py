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

fig, ax = canvas(66)
cw = 7
text(ax, 44, 63, 'bleu : un 1 ; gris : un 0', 'sujet', 's')
text(ax, 44, 58.5, 'orange : colonne × ligne', 'varie', 's')
xs = [6, 28, 50]
def row(y, A, Bm, C, labs, cres):
    mat(ax, xs[0], y, cw, **A); mat(ax, xs[1], y, cw, **Bm); mat(ax, xs[2], y, cw, **C)
    text(ax, 24, y + cw, '×', 'encre', 'xl'); text(ax, 46, y + cw, '=', 'encre', 'xl')
    for x, lab, role in zip(xs, labs, ['sujet', 'sujet', cres]):
        text(ax, x + cw, y - 4, lab, role, 'm')
row(36, dict(ones={(0, 0): 'sujet'}, tint={(1, 0): 'varie'}), dict(ones={(0, 1): 'sujet'}, tint={(0, 0): 'varie'}),
    dict(ones={(0, 1): 'resultat'}), [r'$e_{11}$', r'$e_{12}$', r'$e_{12}$'], 'resultat')
text(ax, 35, 27.5, 'mais', 'limite', 'm', weight='bold')
row(8, dict(ones={(0, 1): 'sujet'}, tint={(1, 1): 'varie'}), dict(ones={(0, 0): 'sujet'}, tint={(1, 0): 'varie', (1, 1): 'varie'}),
    dict(), [r'$e_{12}$', r'$e_{11}$', r'$0$'], 'fixe')
save(fig, '51-213')
