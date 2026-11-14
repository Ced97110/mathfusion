import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
bw = 11
text(ax, 44, 75, r'départ : $3 \times (2 + 5)$ = $(2+5)+(2+5)+(2+5)$', 'encre', 's')
for g in range(3):
    for k, (v, r) in enumerate((('2', 'varie'), ('5', 'autre'))):
        box(ax, 6 + g * 27 + k * (bw + 1), 56, bw, 8, r, label=v)
for i in range(6):
    v, r = (('2', 'varie') if i < 3 else ('5', 'autre'))
    box(ax, 6 + i * 12.5 + (3 if i >= 3 else 0), 32, bw, 8, r, label=v)
# arrows from each source box to its grouped place: 2 stay orange, 5 stay violet
for g in range(3):
    arrow(ax, (6 + g * 27 + bw / 2, 55), (6 + g * 12.5 + bw / 2, 41.5), 'varie', lw=0.7)
    arrow(ax, (6 + g * 27 + bw + 1 + bw / 2, 55), (6 + (3 + g) * 12.5 + 3 + bw / 2, 41.5), 'autre', lw=0.7)
text(ax, 44, 21, "les flèches : on change l'ordre", 'fixe', 's')
brace(ax, 6, 6 + 2 * 12.5 + bw, 31, 'varie', r'$3 \times 2$', down=True)
brace(ax, 6 + 3 * 12.5 + 3, 6 + 5 * 12.5 + 3 + bw, 31, 'autre', r'$3 \times 5$', down=True)
text(ax, 44, 10, r'$3 \times 2 + 3 \times 5 = 6 + 15 = 21$', 'resultat', 'm')
save(fig, '10-056')
