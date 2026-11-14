import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cw = [12, 12, 22, 22]; x0 = 14; xs = []
x = x0
for w in cw:
    xs.append(x); x += w + 1
hdr = [r'$x_1$', r'$x_2$', r'$x_1^2+x_2^2$', r'$x_1-x_2$']
roles = ['sujet', 'sujet', 'resultat', 'varie']
for k in range(4):
    text(ax, xs[k] + cw[k] / 2, 58, hdr[k], roles[k] if k > 1 else 'sujet', 's')
rows = [('Léa', (2, 3)), ('Théo', (3, 2))]
for r, (name, (a, b)) in enumerate(rows):
    y = 34 - r * 20
    text(ax, 7, y + 7, name, 'autre', 'm')
    vals = [a, b, a * a + b * b, a - b]
    for k in range(4):
        role = 'sujet' if k < 2 else roles[k]
        s = str(vals[k]).replace('-', '−')
        box(ax, xs[k], y, cw[k], 14, role, label=s, size='l')
text(ax, 44, 6, 'même 13 ; −1 contre 1', 'fixe', 's')
save(fig, '55-063')
