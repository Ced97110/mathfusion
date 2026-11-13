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
s, x0, yt = 8, 30, 40
for r in range(4):
    for c in range(4):
        if (r, c) != (3, 2): ax.add_patch(Rectangle((x0 + c * s, yt - (r + 1) * s), s, s, ec=COL['fixe'], fc='white', lw=0.6, zorder=2))
ax.add_patch(Rectangle((x0 + 2 * s, yt - 4 * s), s, s, ec=COL['resultat'], fc=FILL['resultat'], lw=1.7, zorder=3))
heads(ax, x0, yt, s)
text(ax, x0 - 4.5, yt + 4.5, '+', 'encre', 'l', weight='bold')
text(ax, x0 + 2 * s + s / 2, yt - 3.5 * s, '1', 'resultat', 'm', weight='bold')
line(ax, [(x0 - 0.5, yt - 3.5 * s), (x0 + 2 * s, yt - 3.5 * s)], 'varie', dash=True, lw=1.1)
line(ax, [(x0 + 2.5 * s, yt + 0.5), (x0 + 2.5 * s, yt - 3 * s)], 'varie', dash=True, lw=1.1)
text(ax, 11, yt + 4.5, 'opération', 'encre', 's')
arrow(ax, (18.5, yt + 4.5), (x0 - 7, yt + 4.5), 'fixe')
text(ax, 77, yt + 4.5, 'termes', 'sujet', 's')
arrow(ax, (70, yt + 4.5), (x0 + 4 * s + 1, yt + 4.5), 'sujet')
text(ax, 11, yt - 2 * s, 'termes', 'sujet', 's')
arrow(ax, (18.5, yt - 2 * s), (x0 - 7.5, yt - 2 * s), 'sujet')
text(ax, x0 + 2.5 * s, 3.5, 'résultat', 'resultat', 's', weight='bold')
arrow(ax, (x0 + 2.5 * s, 6), (x0 + 2.5 * s, yt - 4 * s - 0.3), 'resultat')
save(fig, '51-013')
