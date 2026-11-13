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
s, x0, yt = 9, 9, 44
grid(ax, x0, yt, s, MUL, hl=[(3, 3)])
heads(ax, x0, yt, s)
text(ax, x0 - 4.5, yt + 4.5, '×', 'encre', 'l', weight='bold')
text(ax, x0 + 3.5 * s, yt - 3.5 * s, '1', 'encre', 'm', weight='bold')
arrow(ax, (x0 - 0.8, yt - 3.5 * s), (x0 + 3 * s - 0.3, yt - 3.5 * s), 'varie')
arrow(ax, (x0 + 3.5 * s, yt - 0.2), (x0 + 3.5 * s, yt - 3 * s + 0.3), 'varie')
text(ax, 67, 39, '3 × 3 = 9', 'fixe', 'l')
text(ax, 67, 32, 'aucune case ne contient 9', 'limite', 's')
text(ax, 67, 22, '9 − 8 = 1', 'resultat', 'l', weight='bold')
text(ax, 67, 15, 'la case contient 1', 'resultat', 's')
save(fig, '51-015')
