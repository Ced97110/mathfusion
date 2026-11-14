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
s, x0, yt = 9, 12, 40
twos = [(r, c) for r in range(4) for c in range(4) if MUL(r, c) == 2]
grid(ax, x0, yt, s, MUL, hl=twos)
heads(ax, x0, yt, s)
text(ax, x0 - 4.5, yt + 4.5, '×', 'encre', 'l', weight='bold')
for v in range(4):
    y = 36 - 9.5 * v
    box(ax, 64, y, 18, 8, VAL[v], label=str(v), size='m', weight='bold', lw=1.7 if v == 2 else 0.8)
    if v == 2: ax.add_patch(Rectangle((64, y), 18, 8, ec=COL['encre'], fc='none', lw=1.7, zorder=4))
text(ax, 73, 49, 'couleur = valeur', 'encre', 's')
save(fig, '51-016')
