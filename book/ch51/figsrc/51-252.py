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
text(ax, 44, 74, r'$(1 + \sqrt{2}) \times (-1 + \sqrt{2})$', 'encre', 'l')
X0, CW, CH, YT = 30.0, 24.0, 11.0, 56.0
cols = ['$-1$', r'$\sqrt{2}$']
rows = ['$1$', r'$\sqrt{2}$']
prod = [[('$-1$', 'sujet'), (r'$+\sqrt{2}$', 'varie')], [(r'$-\sqrt{2}$', 'varie'), ('$+2$', 'sujet')]]
for j, c in enumerate(cols):
    text(ax, X0 + CW * (j + 0.5), YT + 5, c, 'autre', 'm')
for i, r in enumerate(rows):
    text(ax, X0 - 6, YT - CH * (i + 0.5), r, 'sujet', 'm')
    for j in range(2):
        lab, role = prod[i][j]
        box(ax, X0 + CW * j + 0.6, YT - CH * (i + 1) + 0.6, CW - 1.2, CH - 1.2, role, label=lab, r=0.6)
text(ax, 44, 28, r'les deux cases en $\sqrt{2}$ s’annulent', 'varie', 'm')
box(ax, 24, 6, 40, 12, 'resultat', label=r'$-1 + 2 = 1$', size='l')
save(fig, '51-252')
