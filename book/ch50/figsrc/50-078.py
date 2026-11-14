import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 3, 62, 36, 12, 'sujet', label=r'$H$ normal dans $G$', size='s')
box(ax, 49, 62, 36, 12, 'sujet', label=r'$N(H) = G$', size='m')
arrow(ax, (40, 68), (48, 68), 'resultat', both=True, lw=1.4)
text(ax, 44, 78, 'même chose', 'resultat', 's')
cw = 9; gap = 1; x0 = 8
for y, lab, n, role in [(36, r'$H$ = les 3 rotations', 6, 'resultat'), (12, r'$H = \{e,\ s_A\}$', 2, 'limite')]:
    text(ax, 3, y + 17, lab, 'autre', 's', ha='left')
    for i in range(6):
        box(ax, x0 + i * (cw + gap), y + 3, cw, 9, 'sujet' if i < n else 'fixe', r=0.5)
    text(ax, 78, y + 7.5, f'{n} sur 6', role, 's', weight='bold')
text(ax, 44, 3.5, r'cases bleues = éléments de $N(H)$', 'sujet', 's')
save(fig, '50-078')
