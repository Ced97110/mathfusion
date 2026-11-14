import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$A_5$ est simple', 'sujet', 'l', weight='bold')
u = 1.2  # mm par élément
rows = [(50, 1, 'sujet', r'$\{e\}$ : 1 élément, normal'), (34, 5, 'limite', '5-Sylow : 5 éléments'),
        (14, 60, 'sujet', r'$A_5$ : 60 éléments, normal')]
for y, n, r, lab in rows:
    ax.add_patch(Rectangle((8, y), n * u, 5, ec=COL[r], fc=FILL[r], lw=0.8, zorder=2))
    if n == 60: text(ax, 8, y + 8.5, lab, r, 's', ha='left')
    else: text(ax, 8 + n * u + 2, y + 2.5, lab, r, 's', ha='left')
text(ax, 8 + 6 * u + 2, 34 - 3.2, 'ni 1, ni 60 : pas normal', 'limite', 's', ha='left')
text(ax, 44, 7, r'donc $n_5 \neq 1$, d’où $n_5 = 6$', 'resultat', 'm', weight='bold')
save(fig, '50-148')
