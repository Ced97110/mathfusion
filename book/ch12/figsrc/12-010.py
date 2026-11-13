import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for y, u, lab, head in ((54, 10, '1 cm', 'élève 1'), (26, 20, '2 cm', 'élève 2')):
    f = numberline(ax, 10, 10 + 3 * u, y, 0, 3, arrow_right=False)
    disc(ax, f(0), y, 1.7, 'sujet'); text(ax, f(0), y + 4.5, r'$O$', 'sujet', 'm')
    disc(ax, f(3), y, 1.7, 'resultat')
    brace(ax, f(0), f(1), y - 7, 'varie', label='unité ' + lab)
    text(ax, 2, y + 10, head, 'fixe', 's', ha='left')
save(fig, '12-010')
