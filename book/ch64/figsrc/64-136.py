import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cs = 2.8
x0s = [4, 36, 68]
ytop = 56
COLS, ROWS = 6, 10   # 6 x 10 = 60 cases : les 60 éléments de A5

def grid(x0, roles):
    """roles : dict {(rang, colonne): rôle} ; les autres cases sont grises."""
    for r in range(ROWS):
        for c in range(COLS):
            role = roles.get((r, c), 'fixe')
            ax.add_patch(Rectangle((x0 + c * cs, ytop - (r + 1) * cs), cs, cs, ec=COL['fixe'], fc=FILL[role], lw=0.4, zorder=2))

grid(x0s[0], {(0, 0): 'fixe', (0, 1): 'sujet'})
grid(x0s[1], {(0, 1): 'varie'})
grid(x0s[2], {(r, c): 'resultat' for r in range(ROWS) for c in range(COLS)})
# la case (0, 0) est l'identité : contour renforcé dans les deux premières grilles
for x0 in x0s[:2]:
    ax.add_patch(Rectangle((x0, ytop - cs), cs, cs, ec=COL['encre'], fc='none', lw=1.0, zorder=3))

w = COLS * cs
text(ax, 44, 68, r'chaque case est un élément de $A_5$', 'encre', 'm')
text(ax, x0s[0] + w / 2, 21, r'$N\neq\{e\}$', 'sujet', 'm')
text(ax, x0s[1] + w / 2, 19, '$N$ contient\nun 3-cycle', 'varie', 'm')
text(ax, x0s[2] + w / 2, 19, '$N=A_5$\n60 éléments', 'resultat', 'm')
for k, lab in enumerate(['lemme C', 'lemme B']):
    xa = x0s[k] + w + 2
    xb = x0s[k + 1] - 2
    arrow(ax, (xa, 38), (xb, 38), 'fixe')
    text(ax, (xa + xb) / 2, 42.5, lab, 'fixe', 's')
save(fig, '64-136')
