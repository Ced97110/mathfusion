import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
H = [0, 3, 6, 9]; K = [0, 2, 4, 6, 8, 10]
cw, chh, x0, ytop = 10.0, 7.0, 22.0, 46.0
fig, ax = canvas(56)
text(ax, 15, ytop + 4, r'$H+K$', 'encre', 's')
n5 = 0
for j, k in enumerate(K):
    text(ax, x0 + (j + .5) * cw, ytop + 4, str(k), 'autre', 'm', weight='bold')
for i, h in enumerate(H):
    y = ytop - (i + 1) * chh
    text(ax, 15, y + chh / 2, str(h), 'sujet', 'm', weight='bold')
    for j, k in enumerate(K):
        v = (h + k) % 12
        role = 'resultat' if v == 5 else 'fixe'
        ax.add_patch(Rectangle((x0 + j * cw, y), cw, chh, ec=COL['fixe'], fc=FILL[role], lw=0.6, zorder=2))
        if v == 5:
            n5 += 1; text(ax, x0 + (j + .5) * cw, y + chh / 2, '5', 'resultat', 'm', weight='bold')
assert n5 == 2
text(ax, 44, ytop - 4 * chh - 6, r'24 cases = 12 valeurs $\times$ 2', 'encre', 'm')
save(fig, '50-193')
