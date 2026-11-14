import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
assert 12 * 13 + 1 == 157 and 12 * 10 == 120 and 12 * 3 == 36
fig, ax = canvas(80)
s = 78 / 157
x0 = 5
ax.add_patch(Rectangle((x0, 62), 157 * s, 8, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
text(ax, x0 + 78 / 2, 66, 'le nombre 157', 'sujet', 'm')
for k in range(13):
    ax.add_patch(Rectangle((x0 + 12 * k * s, 40), 12 * s, 8, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
r = x0 + 156 * s
ax.add_patch(Rectangle((r, 40), 1 * s, 8, ec=COL['resultat'], fc=COL['resultat'], lw=0.8, zorder=2))
brace(ax, x0, x0 + 120 * s, 39, 'varie', label=r'$12\times10=120$', down=True)
brace(ax, x0 + 120 * s + 0.4, r - 0.4, 39, 'varie', label=r'$12\times3=36$', down=True)
arrow(ax, (r + 0.2, 56), (r + 0.2, 49.5), 'resultat')
text(ax, r - 2, 59, 'reste 1', 'resultat', 's', ha='right')
text(ax, 5, 24, 'on retire des blocs de', 'autre', 's', ha='left')
ax.add_patch(Rectangle((x0 + 38, 22), 12 * s, 5, ec=COL['autre'], fc=FILL['autre'], lw=0.8, zorder=2))
text(ax, x0 + 38 + 12 * s + 2, 24.5, '12, le diviseur', 'autre', 's', ha='left')
text(ax, 44, 8, r'$157=12\times13+1$, et $1<12$', 'resultat', 'm')
save(fig, '54-142')
