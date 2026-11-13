import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
box(ax, 14, 86, 60, 10, 'encre', label=r'$Rx\ \cong\ R\,/\,\mathrm{ann}\ x$', size='l', weight='bold')
cols = [(3, 'sujet', 'groupes : R = ℤ', 'x = classe de (1 ; 0)', 'ann x = idéal (2)', 'R/ann x = ℤ/2ℤ', 'horloge à 2 positions'),
        (45, 'autre', 'quart de tour : R = ℝ[x]', 'x = (2 ; 0,8)', 'ann x = idéal (x² + 1)', 'R/ann x = ℂ', 'nombres complexes')]
for x, role, head, r1, r2, res, sub in cols:
    cx = x + 20
    box(ax, x, 70, 40, 9, role, label=head, size='s', weight='bold')
    box(ax, x, 57, 40, 9, role, label=r1, size='s')
    box(ax, x, 44, 40, 9, role, label=r2, size='s')
    box(ax, x, 26, 40, 11, 'resultat', label=res, size='s', weight='bold')
    text(ax, cx, 20, sub, 'resultat', 's')
    arrow(ax, (cx, 70), (cx, 66.5), 'fixe')
    arrow(ax, (cx, 57), (cx, 53.5), 'fixe')
    arrow(ax, (cx, 44), (cx, 37.5), 'fixe')
arrow(ax, (30, 86), (23, 79.5), 'fixe')
arrow(ax, (58, 86), (65, 79.5), 'fixe')
save(fig, '57-223')
