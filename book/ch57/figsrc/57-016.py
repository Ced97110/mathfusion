import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 39, 56, 'on additionne', 'sujet', 's')
text(ax, 72, 56, 'coefficients', 'varie', 's')
rows = [(40, 'situation 1', '(2, 1) + (−1, 2)', 'ℝ'), (25, 'situation 2', '(2, 1) + (6, 3)', 'ℤ'),
        (10, 'situation 3', 'points du plan', 'expressions en T')]
for y, a, b, c in rows:
    box(ax, 2, y, 19, 11, 'fixe', label=a, size='s')
    box(ax, 23, y, 32, 11, 'sujet', label=b, size='s')
    box(ax, 58, y, 28, 11, 'varie', label=c, size='xl' if c in 'ℝℤ' else 's')
save(fig, '57-016')
