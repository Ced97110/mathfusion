import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 5
def sq(x, n, role):
    for i in range(n):
        for j in range(n):
            ax.add_patch(Rectangle((x + i * u, 22 + j * u), u, u, ec=COL[role], fc=FILL[role], lw=0.5, zorder=2))
sq(4, 3, "fixe"); sq(29, 4, "fixe"); sq(59, 5, "sujet")
text(ax, 24, 33, "+", "encre", "l"); text(ax, 54, 33, "=", "encre", "l")
text(ax, 11.5, 17, "$a^2$ = 9", "fixe", "s"); text(ax, 39, 17, "$b^2$ = 16", "fixe", "s"); text(ax, 71.5, 17, "$c^2$ = 25", "sujet", "s")
text(ax, 44, 6, "25 > 9 et 25 > 16", "resultat", "m")
save(fig, "26-031")
