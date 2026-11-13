import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$H$ = les 3 rotations, $N(H) = G$', 'sujet', 's')
cw = 12; gap = 1; x0 = 44 - (6 * cw + 5 * gap) / 2
names = ['$e$', '$r$', '$r^2$', '$s_A$', '$s_B$', '$s_C$']
for i, n in enumerate(names):
    box(ax, x0 + i * (cw + gap), 38, cw, 11, 'autre' if i < 3 else 'sujet', label=n, size='m')
brace(ax, x0, x0 + 3 * cw + 2 * gap, 50, 'autre', down=False, depth=2.0)
text(ax, x0 + (3 * cw + 2 * gap) / 2, 57, r'$H$', 'autre', 'm', weight='bold')
brace(ax, x0, x0 + 6 * cw + 5 * gap, 37, 'sujet', down=True, depth=2.0)
text(ax, 44, 28, r'$N(H)$ : les 6 éléments $g$', 'sujet', 's')
text(ax, 44, 17, r'chaque $g$ donne $gHg^{-1} = H$', 'resultat', 'm', weight='bold')
text(ax, 44, 8, r'donc $H$ est normal dans $N(H)$', 'resultat', 's')
save(fig, '50-076')
