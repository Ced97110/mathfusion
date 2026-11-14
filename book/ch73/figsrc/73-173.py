import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
rows = [(r'$q=2,\ n=2$', [3, 2], 6), (r'$q=3,\ n=2$', [8, 6], 48), (r'$q=2,\ n=3$', [7, 6, 4], 168)]
for i, (lab, fs, res) in enumerate(rows):
    y = 52 - i * 15
    text(ax, 4, y + 4.5, lab, 'encre', 's', ha='left')
    for j, v in enumerate(fs): box(ax, 28 + j * 15, y, 12, 9, 'sujet', label=str(v))
    text(ax, 28 + len(fs) * 15 + 1, y + 4.5, f'= {res}', 'resultat', 'm', ha='left')
text(ax, 44, 6, r'$n$ facteurs $q^n-q^k$', 'sujet', 'm')
save(fig, '73-173')
