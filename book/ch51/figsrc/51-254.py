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
fig, ax = canvas(96)
CX, W_ = 34, 52
text(ax, CX, 92, 'si le dénominateur était nul', 'sujet', 'm')
box(ax, CX - W_ / 2, 74, W_, 12, 'sujet', label=r'$a^2 - 2b^2 = 0$', size='l')
arrow(ax, (CX, 74), (CX, 61), 'varie', lw=1.3)
text(ax, CX + 3, 67.5, r'on divise par $b^2$', 'varie', 'm', ha='left')
box(ax, CX - W_ / 2, 49, W_, 12, 'sujet', label=r'$(a/b)^2 = 2$', size='l')
arrow(ax, (CX, 49), (CX, 36), 'fixe', lw=1.3)
box(ax, CX - W_ / 2, 24, W_, 12, 'limite', label='impossible (chapitre 22)', size='m')
arrow(ax, (CX, 24), (CX, 14), 'resultat', lw=1.3)
box(ax, CX - W_ / 2, 3, W_, 11, 'resultat', label=r'donc $a^2 - 2b^2 \neq 0$', size='m')
# essais chiffrés
text(ax, 75, 84, 'essais', 'fixe', 'm')
for y, a, b, d in ((72, 1, 1, '−1'), (56, 3, 2, '1')):
    text(ax, 75, y, rf'$a = {a}$, $b = {b}$', 'fixe', 's')
    text(ax, 75, y - 5.5, f'dénominateur {d}', 'fixe', 's')
save(fig, '51-254')
