import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for role, lab, y in [('sujet', r'1,5 $\times$ 10$^6$', 58), ('autre', r'9,5 $\times$ 10$^6$', 46)]:
    text(ax, 4, y + 3.5, lab, role, 'm', ha='left')
    for i in range(7): box(ax, 38 + i * 6.8, y - 1, 6, 9, role)
brace(ax, 38, 38 + 6.8 * 6 + 6, 44, 'fixe', '7 chiffres chacun', down=True)
text(ax, 4, 28, 'mantisses (entre 1 et 10)', 'fixe', 's', ha='left')
f = numberline(ax, 10, 76, 18, 1, 10, labels=False, arrow_right=False)
text(ax, f(1), 13.5, '1', 'fixe', 's'); text(ax, f(10), 13.5, '10', 'fixe', 's')
disc(ax, f(1.5), 18, 1.6, 'sujet'); disc(ax, f(9.5), 18, 1.6, 'autre')
text(ax, f(1.5), 23, '1,5', 'sujet', 's'); text(ax, f(9.5), 23, '9,5', 'autre', 's')
arrow(ax, (f(1.9), 20.5), (f(9.1), 20.5), 'varie', curve=-0.25)
text(ax, f(5.5), 4, r'rapport $\approx$ 6,3 : moins de 10', 'varie', 'm')
save(fig, '14-082')
