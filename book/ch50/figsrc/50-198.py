import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
H = [0, 5, 10]; K = [0, 3, 6, 9, 12]
vals = [(h + k) % 15 for h in H for k in K]; assert sorted(vals) == list(range(15))
cw, chh, x0, ytop = 10.0, 6.5, 22.0, 70.0
fig, ax = canvas(82)
text(ax, 15, ytop + 4, r'$H+K$', 'encre', 's')
for j, k in enumerate(K): text(ax, x0 + (j + .5) * cw, ytop + 4, str(k), 'autre', 'm', weight='bold')
for i, h in enumerate(H):
    y = ytop - (i + 1) * chh
    text(ax, 15, y + chh / 2, str(h), 'sujet', 'm', weight='bold')
    for j in range(5):
        ax.add_patch(Rectangle((x0 + j * cw, y), cw, chh, ec=COL['fixe'], fc=FILL['resultat'], lw=0.6, zorder=2))
text(ax, 44, 44, '15 cases = 15 valeurs', 'resultat', 'm', weight='bold')
f = numberline(ax, 8, 78, 28, 0, 14, 1, arrow_right=False, every=5)
for v in range(15): disc(ax, f(v), 28, 1.3, 'resultat')
text(ax, 44, 8, r'$H\cap K=\{0\}$', 'encre', 'm')
save(fig, '50-198')
