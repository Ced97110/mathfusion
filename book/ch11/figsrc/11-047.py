import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
names = ['kilo', 'hecto', 'déca', 'base', 'déci', 'centi', 'milli']
w, g = 10.5, 1.5
xs = [2.75 + i * (w + g) for i in range(7)]
for i, n in enumerate(names):
    role = 'sujet' if i == 0 else ('resultat' if i == 3 else 'fixe')
    box(ax, xs[i], 26, w, 9, role, label=n, size='s')
for i in range(3):
    p = (xs[i] + w / 2, 36.5); q = (xs[i + 1] + w / 2, 36.5)
    arrow(ax, p, q, 'varie', curve=-0.7)
    text(ax, (p[0] + q[0]) / 2, 44, str(i + 1), 'varie', 's')
text(ax, 44, 57, 'un pas vers la droite :', 'encre', 's')
text(ax, 44, 52, 'unité ÷ 10, nombre × 10', 'varie', 's')
text(ax, 44, 12, '3 kg = 3 000 g', 'resultat', 'l')
text(ax, 44, 5, 'trois pas, puis on s’arrête sur la base', 'encre', 's')
save(fig, '11-047')
