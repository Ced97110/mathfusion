import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def parts(x, y, w, h, n, k, role):
    for i in range(n):
        ax.add_patch(Rectangle((x + i * w / n, y), w / n, h, ec=COL[role], fc=FILL[role] if i < k else FILL['encre'], lw=0.6, zorder=2))
fig, ax = canvas(72)
text(ax, 23, 68, 'exact : on cherche', 'sujet', 'm')
text(ax, 66, 68, 'estimation : on choisit', 'varie', 'm')
text(ax, 3, 60, '3/5', 'sujet', 'm', ha='left'); parts(3, 52, 40, 6, 5, 3, 'sujet')
text(ax, 3, 46, '5/12', 'autre', 'm', ha='left'); parts(3, 38, 40, 6, 12, 5, 'autre')
text(ax, 23, 31, '1/5 et 1/12 : parts inégales', 'fixe', 's')
text(ax, 23, 24, 'on cherche des parts de 1/60', 'varie', 's')
text(ax, 23, 14, '= 61/60', 'resultat', 'l')
text(ax, 47, 60, '3/5 ≈ 1/2', 'sujet', 'm', ha='left'); parts(47, 52, 38, 6, 2, 1, 'sujet')
text(ax, 47, 46, '5/12 ≈ 1/2', 'autre', 'm', ha='left'); parts(47, 38, 38, 6, 2, 1, 'autre')
text(ax, 66, 31, 'parts égales : 1/2', 'fixe', 's')
text(ax, 66, 14, '1/2 + 1/2 = 1', 'resultat', 'l')
save(fig, '10-067')
