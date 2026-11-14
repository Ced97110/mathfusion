import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cw, ch, x0, ytop = 11, 8, 4, 50
for i in range(5):
    for j in range(5):
        poly(ax, [(x0 + j * cw, ytop - (i + 1) * ch), (x0 + (j + 1) * cw, ytop - (i + 1) * ch),
                  (x0 + (j + 1) * cw, ytop - i * ch), (x0 + j * cw, ytop - i * ch)], 'fixe', lw=0.5)
text(ax, x0 + 2.5 * cw, ytop + 4, r'cases grises : $0$', 'fixe', 's')
bars = [(0, 0, 4, '1   2   3   4', 'sujet'), (1, 1, 4, '1   2   3   4', 'sujet'),
        (2, 0, 3, '1   5   6', 'autre'), (3, 1, 3, '1   5   6', 'autre'), (4, 2, 3, '1   5   6', 'autre')]
for i, j, k, s, role in bars:
    box(ax, x0 + j * cw + 0.5, ytop - (i + 1) * ch + 0.5, k * cw - 1, ch - 1, role, label=s, size='s', r=0.5)
xb = x0 + 5 * cw + 2
line(ax, [(xb, ytop - 0.5), (xb, ytop - 2 * ch + 0.5)], 'sujet', lw=1.2)
line(ax, [(xb, ytop - 2 * ch - 0.5), (xb, ytop - 5 * ch + 0.5)], 'autre', lw=1.2)
text(ax, xb + 2, ytop - ch, r'$m=2$ lignes de $f$', 'sujet', 's', ha='left')
text(ax, xb + 2, ytop - 3.5 * ch, r'$n=3$ lignes de $g$', 'autre', 's', ha='left')
text(ax, x0 + 2.5 * cw, ytop - 5 * ch - 4, r'$m+n=5$ colonnes', 'fixe', 's')
save(fig, '70-038')
