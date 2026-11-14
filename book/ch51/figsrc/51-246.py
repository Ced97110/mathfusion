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
fig, ax = canvas(80)
M = dict(A=[[1, 1], [1, 0]], B=[[0, 1], [1, 1]], I=[[1, 0], [0, 1]])
ROLE = dict(A='sujet', B='autre', I='fixe')
c = (14, 42, 74)
def op_plus(x, y):
    line(ax, [(x - 2, y), (x + 2, y)], 'encre', lw=1.0); line(ax, [(x, y - 2), (x, y + 2)], 'encre', lw=1.0)
def op_eq(x, y):
    line(ax, [(x - 2, y + 0.9), (x + 2, y + 0.9)], 'encre', lw=1.0); line(ax, [(x - 2, y - 0.9), (x + 2, y - 0.9)], 'encre', lw=1.0)
def eq(cy, a, b, r, hot):
    for cx in c:
        for (i, j) in hot:
            x, y = cell(cx, cy, i, j); hl(ax, x - 2.0, y - 1.7, 4.0, 3.4)
    for cx, nm in zip(c, (a, b, r)):
        mat(ax, cx, cy, M[nm], ROLE[nm])
        text(ax, cx, cy - 9, f'${nm}$', ROLE[nm], 'l')
    op_plus(28, cy); op_eq(58, cy)
eq(64, 'A', 'B', 'I', [(0, 1), (1, 0)])
eq(34, 'A', 'I', 'B', [(0, 0)])
text(ax, 44, 8, r'cases orange : $1 + 1 = 0$', 'varie', 'm')
save(fig, '51-246')
