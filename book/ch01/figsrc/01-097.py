import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
f = numberline(ax, 8, 80, 16, 4300, 4400, step=10, labels=False, arrow_right=False)
text(ax, 8, 11.5, '4 300', 'fixe', 's'); text(ax, 80, 11.5, '4 400', 'fixe', 's')
for k in range(10):
    x = 8 + 7.2 * k
    r = 'autre' if k < 5 else 'varie'
    box(ax, x, 19, 7.2, 8, r, label=str(k), size='m', r=0.5)
text(ax, 8, 31, 'chiffre témoin (dizaines)', 'encre', 's', ha='left')
line(ax, [(44, 13), (44, 36)], 'sujet', lw=1.4)
disc(ax, 44, 16, 0.9, 'sujet')
text(ax, 44, 39.5, 'milieu 4 350', 'sujet', 'm')
arrow(ax, (26, 6), (9, 6), 'autre')
arrow(ax, (62, 6), (79, 6), 'varie')
save(fig, '01-097')
