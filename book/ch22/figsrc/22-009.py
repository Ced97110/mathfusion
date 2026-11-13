import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 6.0
y0 = 22
items = ((4, 'aire 16\ncôté 4', 6), (3, 'aire 9\ncôté 3', 38), (2 ** 0.5, 'aire 2\ncôté ?', 66))
for side, lab, x in items:
    poly(ax, [(x, y0), (x+side*u, y0), (x+side*u, y0+side*u), (x, y0+side*u)], 'sujet')
    text(ax, x + side*u/2, y0 - 6, lab, 'sujet', 's')
text(ax, 44, 56, 'quel côté pour cette aire ?', 'encre', 'm')
save(fig, '22-009')
