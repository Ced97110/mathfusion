import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 7
rows = (("$a$ = 3", 3, "fixe", ""), ("$b$ = 4", 4, "fixe", ""), ("$c$ = 4 ?", 4, "limite", "16 ≠ 25"), ("$c$ = 5", 5, "resultat", "25 = 9 + 16"))
for i, (lab, n, role, res) in enumerate(rows):
    y = 42 - i * 12
    text(ax, 3, y + 2.5, lab, role, "m", ha="left")
    ax.add_patch(Rectangle((24, y), n * u, 5, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    if res: text(ax, 24 + n * u + 3, y + 2.5, res, role, "s", ha="left")
text(ax, 44, 5, "l'hypoténuse dépasse chaque côté", "resultat", "s") if False else None
save(fig, "26-032")
