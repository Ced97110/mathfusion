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
fig, ax = canvas(72)
def ligne(y, role, labels):
    xs = [(2, 24), (32, 54), (63, 86)]
    for (x0, x1), lab in zip(xs, labels):
        box(ax, x0, y, x1 - x0, 16, role, label=lab, size='l')
    ym = y + 8
    line(ax, [(25.5, ym + 1), (30.5, ym + 1)], 'encre', lw=1.0); line(ax, [(25.5, ym - 1), (30.5, ym - 1)], 'encre', lw=1.0)
    line(ax, [(56, ym), (61, ym)], 'encre', lw=1.0)
text(ax, 44, 66, r'formule pour tous $a$ et $b$', 'sujet', 'm')
ligne(44, 'sujet', [r'$\dfrac{1}{a+b\sqrt{2}}$', r'$\dfrac{a}{a^2-2b^2}$', r'$\dfrac{b}{a^2-2b^2}\sqrt{2}$'])
arrow(ax, (44, 42), (44, 33), 'varie')
text(ax, 47, 37.5, r'$a = 3$ et $b = 1$', 'varie', 'm', ha='left')
ligne(14, 'varie', [r'$\dfrac{1}{3+\sqrt{2}}$', r'$\dfrac{3}{7}$', r'$\dfrac{1}{7}\sqrt{2}$'])
text(ax, 44, 6, r'dénominateur : $9 - 2 = 7$', 'varie', 'm')
save(fig, '51-253')
