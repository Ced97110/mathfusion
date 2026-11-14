import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
GX, SY = 2.08, 1.78
def mat(ax, cx, cy, M, role='sujet'):
    t = text(ax, cx, cy, f'{M[0][0]}   {M[0][1]}\n{M[1][0]}   {M[1][1]}', role, 'm'); t.set_linespacing(1.5)
    for s in (-1, 1):
        x = cx + s * 4.6
        line(ax, [(x - s * 1.2, cy + 4.4), (x, cy + 4.4), (x, cy - 4.4), (x - s * 1.2, cy - 4.4)], role, lw=0.8)
def cell(cx, cy, r, c): return (cx + (c - 0.5) * 2 * GX, cy + (0.5 - r) * 2 * SY)
def hl(ax, x, y, w, h, role='varie'):
    ax.add_patch(Rectangle((x, y), w, h, fc=FILL[role], ec=COL[role], lw=0.6, zorder=1))
fig, ax = canvas(66)
R = 3.4
def ligne(y, labels, role, titre, comptage):
    xs = [14 + 14 * k for k in range(len(labels))]
    text(ax, 2, y + 11, titre, role, 'm', ha='left')
    for k, (x, lab) in enumerate(zip(xs, labels)):
        last = k == len(labels) - 1
        disc(ax, x, y, R, 'resultat' if last else role, label=lab)
        if k: arrow(ax, (xs[k - 1] + R, y), (x - R, y), 'varie')
    text(ax, (xs[0] + xs[-1]) / 2, y - 8.5, comptage, 'varie', 'm')
ligne(48, ['0', '$I$', '0'], 'sujet', r'$F$ : chaque saut ajoute $I$', '2 sauts pour revenir à 0')
ligne(18, ['0', '1', '2', '3', '0'], 'autre', 'ℤ/4 : chaque saut ajoute 1', '4 sauts pour revenir à 0')
save(fig, '51-249')
