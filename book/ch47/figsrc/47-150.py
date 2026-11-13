import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cs = [16, 44, 72]
for i, (a, b, d) in enumerate([('14', '2', '−12'), ('15', '3', '−12'), ('29', '5', '−24')]):
    box(ax, cs[i] - 9, 46, 18, 11, 'sujet', label=a)
    box(ax, cs[i] - 9, 20, 18, 11, 'autre', label=b)
    arrow(ax, (cs[i], 46), (cs[i], 32), 'varie')
    text(ax, cs[i] + 2.5, 39, d, 'varie', 's', ha='left')
for x, s in [(30, '+'), (58, '=')]:
    text(ax, x, 51.5, s, 'encre', 'l'); text(ax, x, 25.5, s, 'encre', 'l')
box(ax, 8, 4, 72, 11, 'resultat', label='29 − 5 = 24 : multiple de 12', size='s')
save(fig, '47-150')
