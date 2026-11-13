import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
vals = [1, 1, 3, 4, 1, 2, 1, 2, 1, 1]
x0, w, g = 4.5, 6.6, 1.7
for i, v in enumerate(vals):
    role = 'varie' if v == 4 else 'sujet'
    for k in range(v):
        box(ax, x0 + i * (w + g), 14 + k * 7.2, w, 6.6, role, r=0.4)
    text(ax, x0 + i * (w + g) + w / 2, 9, str(v), role, 'm')
brace(ax, x0, x0 + 10 * (w + g) - g, 4.5, 'fixe', None, depth=1.2)
text(ax, 44, 50, "1 + 1 + 3 + 4 + 1 + 2 + 1 + 2 + 1 + 1", "encre", "m")
box(ax, 26, 53.5, 36, 7, 'resultat', label='= 17 groupes', size='m')
save(fig, '74-164')
