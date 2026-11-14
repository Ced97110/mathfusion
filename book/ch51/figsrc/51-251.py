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
text(ax, 19, 58, 'nombre à inverser', 'sujet', 'm')
text(ax, 69, 58, 'son conjugué', 'varie', 'm')
box(ax, 4, 40, 30, 12, 'sujet', label=r'$1 + \sqrt{2}$', size='l')
box(ax, 54, 40, 30, 12, 'varie', label=r'$1 - \sqrt{2}$', size='l')
text(ax, 44, 46, r'$\times$', 'encre', 'l')
text(ax, 69, 35, 'signe changé', 'varie', 's')
arrow(ax, (44, 38), (44, 25), 'fixe')
text(ax, 47, 31.5, 'produit', 'fixe', 's', ha='left')
box(ax, 24, 11, 40, 12, 'resultat', label=r'$1 - 2 = -1$', size='l')
text(ax, 44, 5, r'plus de $\sqrt{2}$ : on s’arrête', 'resultat', 'm')
save(fig, '51-251')
