import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 2, 68, 'sous-groupe', 'fixe', 's', ha='left')
cols = [38, 52, 66, 80]
for x, h in zip(cols, ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$']):
    text(ax, x, 68, h, 'encre', 'm')
rows = [(r'$G$', [0, 1, 2, 3]), (r'$\langle\sigma\rangle$', [0, 1]), (r'$\langle\tau\rangle$', [0, 2]),
        (r'$\langle\sigma\tau\rangle$', [0, 3]), (r'$\{1\}$', [0])]
for i, (lab, members) in enumerate(rows):
    y = 56 - 12 * i
    line(ax, [(2, y - 6), (86, y - 6)], 'fixe', lw=0.4)
    text(ax, 2, y, lab, 'encre', 'm', ha='left')
    for k in members:
        disc(ax, cols[k], y, 2.6, 'sujet')
save(fig, '63-020')
