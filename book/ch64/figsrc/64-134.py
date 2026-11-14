import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ys = [52, 36, 20, 4]
H = 12
conds = ['un cycle de 4 objets ou +', 'sinon : deux 3-cycles ou +', 'sinon : un seul 3-cycle', 'sinon : aucun 3-cycle']
cases = ['cas 2', 'cas 3', 'cas 1 ou 4', 'cas 5']

def link(pts, closed=True):
    q = list(pts) + ([pts[0]] if closed and len(pts) > 2 else [])
    line(ax, q, 'sujet', lw=0.7)
    for p in pts:
        ax.add_patch(Circle(p, 1.4, ec=COL['sujet'], fc=FILL['sujet'], lw=0.7, zorder=3))

def tri(cx, cy):
    link([(cx, cy + 2.6), (cx - 2.6, cy - 1.8), (cx + 2.6, cy - 1.8)])

def pair(cx, cy):
    link([(cx - 2.6, cy), (cx + 2.6, cy)], closed=False)

text(ax, 44, 69, 'chaque permutation : une seule case', 'encre', 'm')
for k, y in enumerate(ys):
    box(ax, 2, y, 84, H, 'fixe')
    cy = y + H / 2
    if k == 0:
        link([(13.5, cy + 2.8), (18.5, cy + 2.8), (18.5, cy - 2.8), (13.5, cy - 2.8)])
    elif k == 1:
        tri(10, cy); tri(22, cy)
    elif k == 2:
        tri(10, cy); pair(22, cy)
    else:
        pair(10, cy); pair(22, cy)
    text(ax, 31, cy, conds[k], 'encre', 's', ha='left')
    text(ax, 78, cy, cases[k], 'sujet', 'm', weight='bold')
    if k < 3:
        arrow(ax, (44, y - 0.2), (44, y - 3.8), 'fixe', lw=0.8)
save(fig, '64-134')
