import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for i in range(6):
    for j in range(6): ax.add_patch(Rectangle((6 + 7*i, 6 + 7*j), 7, 7, ec=COL['fixe'], fc=FILL['fixe'], lw=0.4, zorder=2))
for bi in range(3):
    for bj in range(3):
        hot = (bi == 2 and bj == 1)
        ax.add_patch(Rectangle((6 + 14*bi, 6 + 14*bj), 14, 14, ec=COL['varie' if hot else 'sujet'], fc=FILL['varie'] if hot else 'none', lw=1.3, zorder=3))
brace(ax, 6, 48, 48, 'fixe', label=r'$ab = 6$', down=False)
text(ax, 70, 40, r'$a^2 = 9$ blocs', 'sujet'); arrow(ax, (56, 40), (44, 41), 'sujet')
text(ax, 70, 27, r'$b^2 = 4$ carreaux', 'varie'); arrow(ax, (56, 27), (46, 27), 'varie')
text(ax, 70, 12, r'$(ab)^2 = 36$', 'resultat', weight='bold')
save(fig, '14-047')
