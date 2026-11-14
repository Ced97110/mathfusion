import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
VAL = ["encre", "sujet", "varie", "resultat"]
def cell(ax, x, y, s, v, hl=False):
    ax.add_patch(Rectangle((x, y), s, s, ec=COL["encre"] if hl else COL["fixe"], fc=FILL[VAL[v]], lw=1.7 if hl else 0.6, zorder=3 if hl else 2))
def grid(ax, x0, ytop, s, op, hl=()):
    for r in range(4):
        for c in range(4):
            if (r, c) not in hl: cell(ax, x0 + c * s, ytop - (r + 1) * s, s, op(r, c))
    for (r, c) in hl: cell(ax, x0 + c * s, ytop - (r + 1) * s, s, op(r, c), True)
def heads(ax, x0, ytop, s, top=True, left=True, role="sujet"):
    for k in range(4):
        if top: text(ax, x0 + k * s + s / 2, ytop + 4.5, str(k), role, "s", weight="bold")
        if left: text(ax, x0 - 4.5, ytop - k * s - s / 2, str(k), role, "s", weight="bold")
ADD = lambda r, c: (r + c) % 4
MUL = lambda r, c: (r * c) % 4
fig, ax = canvas(54)
s, yt = 7.2, 40
grid(ax, 9, yt, s, ADD)
grid(ax, 43, yt, s, MUL, hl=[(2, 0), (2, 1), (2, 2), (2, 3)])
heads(ax, 9, yt, s, top=True, left=True)
heads(ax, 43, yt, s, top=True, left=False)
text(ax, 4.5, yt + 4.5, '+', 'encre', 'l', weight='bold')
text(ax, 38.5, yt + 4.5, '×', 'encre', 'l', weight='bold')
yr = yt - 2.5 * s
arrow(ax, (76, yr), (72.8, yr), 'encre', lw=1.0)
text(ax, 77.2, yr - 0.5, 'que\n0 et 2', 'encre', 's', ha='left')
save(fig, '51-012')
