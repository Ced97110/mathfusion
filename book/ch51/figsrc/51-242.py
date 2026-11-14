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
fig, ax = canvas(60)
text(ax, 44, 55, '16 tableaux possibles, 4 gardés', 'fixe', 's')
els = [('0', [[0, 0], [0, 0]]), ('I', [[1, 0], [0, 1]]), ('A', [[1, 1], [1, 0]]), ('B', [[0, 1], [1, 1]])]
for k, (nm, M) in enumerate(els):
    cx = 14 + 20 * k
    mat(ax, cx, 38, M, 'sujet')
    text(ax, cx, 28.5, nm if nm == '0' else f'${nm}$', 'sujet', 'l')
brace(ax, 6, 82, 25, 'sujet', label=r'$F$ : 4 éléments', size='m')
text(ax, 44, 8, r'cases dans ℤ/2 : $1 + 1 = 0$', 'varie', 'm')
save(fig, '51-242')
