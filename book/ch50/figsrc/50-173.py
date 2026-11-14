import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [(60, r'$n_5$ divise 3', [('3', 'limite'), ('1', 'resultat')], r'$n_5=1$'),
        (44, r'$n_3$ divise 5', [('5', 'limite'), ('1', 'resultat')], r'$n_3=1$'),
        (28, r'$|P\cap Q|$ divise 3 et 5', [('1', 'resultat')], r'$|P\cap Q|=1$'),
        (12, "3 et 5 divisent l'ordre", [], r'$xy$ : ordre 15')]
for y, lab, chips, res in rows:
    text(ax, 3, y + 4.5, lab, 'encre', 's', ha='left')
    for i, (c, r) in enumerate(chips[::-1] if False else chips):
        x = 46 + 9 * i if len(chips) == 2 else 55
        box(ax, x, y, 8, 9, r, label=c)
        if r == 'limite': line(ax, [(x + 1, y + 1.5), (x + 7, y + 7.5)], 'limite', lw=1.1)
    arrow(ax, (65, y + 4.5), (68, y + 4.5), 'resultat')
    box(ax, 68, y, 18, 9, 'resultat', label=res, size='s')
save(fig, '50-173')
