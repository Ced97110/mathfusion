import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
assert (2 + 3 * 2 + 1 * 4) == 12 and 12 % 5 == 2 and 7 % 5 == 2
steps = [(r'$A=7+3x+1x^2$', 'sujet', 74),
         (r'$2+3x+1x^2$', 'varie', 54),
         (r'$2+3\times2+1\times4$', 'varie', 34),
         (r'$12=2$ dans ℤ/5', 'resultat', 14)]
for t, role, y in steps:
    box(ax, 4, y, 44, 10, role, label=t, size='m')
notes = [r'$\eta$ : 7 devient 2', r'$x$ devient $u=2$', 'on calcule dans ℤ/5']
for i, n in enumerate(notes):
    y0 = steps[i][2]
    arrow(ax, (26, y0 - 0.5), (26, y0 - 9.5), 'varie')
    text(ax, 30, y0 - 5, n, 'varie', 's', ha='left')
save(fig, '54-107')
