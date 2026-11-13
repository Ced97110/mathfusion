import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw, ch, gp = 15, 8, 2
x0 = (88 - (5 * cw + 4 * gp)) / 2
terms = [(r'$-3a$', 'sujet'), (r'$2b$', 'autre'), (r'$-5a$', 'sujet'), (r'$a$', 'sujet'), (r'$6b$', 'autre')]
order = [0, 2, 3, 1, 4]
X = [x0 + i * (cw + gp) for i in range(5)]
text(ax, 44, 69, 'mélangés', 'fixe', 'm')
for i, (t, r) in enumerate(terms): box(ax, X[i], 56, cw, ch, r, label=t)
for j, i in enumerate(order):
    box(ax, X[j], 26, cw, ch, terms[i][1], label=terms[i][0])
    arrow(ax, (X[i] + cw / 2, 55.5), (X[j] + cw / 2, 34.5), 'varie')
brace(ax, X[0] + 0.5, X[2] + cw - 0.5, 25.4, 'sujet', r'$-7a$')
brace(ax, X[3] + 0.5, X[4] + cw - 0.5, 25.4, 'autre', r'$8b$')
text(ax, 44, 12, 'regroupés par famille', 'fixe', 'm')
save(fig, '15-051')
