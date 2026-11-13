import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
assert 5 * 3 + 2 == 17
cw, x0 = 4.6, 4.7
for i in range(17):
    ax.add_patch(Rectangle((x0 + cw * i, 42), cw, 7, ec=COL['sujet' if i < 15 else 'resultat'],
                           fc=FILL['sujet' if i < 15 else 'resultat'], lw=0.7, zorder=2))
brace(ax, x0, x0 + 17 * cw, 51, 'fixe', label=r'$a = 17$', down=False)
for g in range(3):
    brace(ax, x0 + g * 5 * cw + 0.4, x0 + (g + 1) * 5 * cw - 0.4, 41, 'sujet', label=r'$b = 5$')
brace(ax, x0 + 15 * cw + 0.4, x0 + 17 * cw, 41, 'resultat', label=r'$r = 2$')
text(ax, x0 + 7.5 * cw, 30, r'$q = 3$ groupes de $b$', 'sujet', 's')
for k, (n, role, y) in enumerate([(5, 'autre', 15), (2, 'resultat', 6)]):
    for i in range(n):
        ax.add_patch(Rectangle((x0 + cw * i, y), cw, 6, ec=COL[role], fc=FILL[role], lw=0.7, zorder=2))
text(ax, x0 + 5 * cw + 2, 18, 'taille de b : 5', 'autre', 's', ha='left')
text(ax, x0 + 5 * cw + 2, 9, 'taille de r : 2', 'resultat', 's', ha='left')
text(ax, 74, 13.5, r'$\delta(r) < \delta(b)$', 'resultat', 's')
save(fig, '56-119')
