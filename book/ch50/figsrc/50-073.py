import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$H \subseteq N(H) \subseteq G$', 'sujet', 'l', weight='bold')
cw = 9; gap = 1.2; x0 = 44 - (6 * cw + 5 * gap) / 2
cases = [(48, r'$H = \{e,\ s_A\}$', 2, 2, '2 éléments'), (20, r'$H$ = les 3 rotations', 3, 6, '6 éléments')]
for y, lab, nH, nN, cnt in cases:
    text(ax, 44, y + 17, lab, 'autre', 's')
    for i in range(6):
        role = 'sujet' if i < nN else 'fixe'
        box(ax, x0 + i * (cw + gap), y + 3, cw, 9, role, r=0.5)
        if i < nH:
            disc(ax, x0 + i * (cw + gap) + cw / 2, y + 7.5, 1.9, 'autre')
    text(ax, 44, y - 2, r'$N(H)$ : ' + cnt, 'sujet', 's')
box(ax, 4, 2, 4, 4, 'sujet', r=0.3)
text(ax, 10, 4, 'dans $N(H)$', 'sujet', 's', ha='left')
disc(ax, 40, 4, 1.9, 'autre'); text(ax, 43.5, 4, 'dans $H$', 'autre', 's', ha='left')
box(ax, 62, 2, 4, 4, 'fixe', r=0.3); text(ax, 68, 4, 'hors $N(H)$', 'fixe', 's', ha='left')
save(fig, '50-073')
