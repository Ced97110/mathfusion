import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
items = [('fixe', 'u dans E, E/F algébrique'), ('varie', 'p minimal de u : irréductible'),
         ('sujet', 'degré 1 : x − a, a dans F'), ('resultat', 'u = a, donc u est dans F')]
h, g, x, w = 11, 6.5, 8, 72
ys = [2 + (3 - i) * (h + g) for i in range(4)]
for (role, s), y in zip(items, ys):
    box(ax, x, y, w, h, role, label=s, size='s')
for i in range(3):
    arrow(ax, (44, ys[i]), (44, ys[i + 1] + h), 'encre')
save(fig, '61-144')
