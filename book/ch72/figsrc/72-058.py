import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'tableau $h$ de $\eta$', 'encre', 'm')
x0, c, hh = 38, 22, 14
rows = [(r'$5/4$', r'$3/4$', 'sujet'), (r'$3/4$', r'$5/4$', 'autre')]
for i, (a, b, r) in enumerate(rows):
    y = 34 - i * (hh + 2)
    box(ax, x0, y, c, hh, r, label=a); box(ax, x0 + c + 1, y, c, hh, r, label=b)
    text(ax, 2, y + hh / 2, 'ligne %d' % (i + 1), r, 's', ha='left')
    arrow(ax, (18, y + hh / 2), (x0 - 1, y + hh / 2), r)
    text(ax, 28, y + hh / 2 + 4, r'$\eta e_%d$' % (i + 1), r, 's')
text(ax, 44, 8, r'ligne $i$ = coordonnées de $\eta e_i$', 'encre', 's')
save(fig, '72-058')
