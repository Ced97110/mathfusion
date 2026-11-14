import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
for y0, role, lab, els in [(40, 'sujet', 'R = N : les rotations', ['1', r'$r$', r'$r^2$', r'$r^3$']),
                           (4, 'varie', 'S = sN : les retournements', [r'$s$', r'$rs$', r'$r^2s$', r'$r^3s$'])]:
    box(ax, 3, y0, 82, 24, role, r=1.2)
    text(ax, 7, y0 + 18.5, lab, role, 'm', ha='left')
    for i, e in enumerate(els):
        disc(ax, 17 + 18 * i, y0 + 8, 5.0, role, label=e, size='s')
text(ax, 44, 33, '8 ÷ 4 = 2 classes', 'resultat', 'm')
save(fig, '47-153')
