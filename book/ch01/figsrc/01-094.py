import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for xc, lab in zip((31, 45, 59, 73), ('milliers', 'centaines', 'dizaines', 'unités')):
    text(ax, xc, 52, lab, 'fixe', 's')
digits = '4329'
for yb, hi, lab in ((36, 1, 'à la centaine'), (18, 2, 'à la dizaine')):
    yc = yb + 5
    text(ax, 3, yc, lab, 'fixe', 's', ha='left')
    for i, d in enumerate(digits):
        box(ax, 24 + 14 * i, yb, 14, 10, 'sujet' if i == hi else 'fixe', label=d, size='l')
poly(ax, [(43, 31), (47, 31), (45, 34.5)], 'varie')
poly(ax, [(57, 13), (61, 13), (59, 16.5)], 'varie')
save(fig, '01-094')
