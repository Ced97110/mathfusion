import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cw, x0 = 7.0, 12.5
text(ax, 44, 83, r'$|Z(G)|=p=3$ ; $G$ : 9 éléments', 'encre', 'm')
for i in range(9):
    role = 'sujet' if i < 3 else ('varie' if i == 3 else 'fixe')
    ax.add_patch(Rectangle((x0 + i * cw, 60), cw, 7, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    ax.add_patch(Rectangle((x0 + i * cw, 33), cw, 7, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
brace(ax, x0, x0 + 4 * cw, 68, 'fixe', r'$C(x)$ : au moins 4 éléments', down=False)
text(ax, x0 + 1.5 * cw, 55.5, r'$Z(G)$', 'sujet', 'm'); text(ax, x0 + 3.5 * cw, 55.5, r'$x$', 'varie', 'm')
arrow(ax, (8, 51), (8, 44), 'varie'); text(ax, 12, 47.5, 'divise 9, dépasse 3 : donc 9', 'varie', 's', ha='left')
text(ax, 44, 29, r'$C(x)=G$', 'resultat', 'm')
text(ax, 44, 19, r'donc $x\in Z(G)$ : absurde', 'limite', 'm')
save(fig, '50-200')
