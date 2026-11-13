import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
names = ['kilo', 'hecto', 'déca', 'base', 'déci', 'centi']
w, g = 11, 2
xs = [2 + i * (w + g) for i in range(6)]
for i, n in enumerate(names):
    role = 'resultat' if i == 3 else ('sujet' if i in (0, 5) else 'fixe')
    box(ax, xs[i], 26, w, 9, role, label=n, size='s')
c = lambda i: xs[i] + w / 2
arrow(ax, (c(0), 36.5), (c(3), 36.5), 'resultat', curve=-0.35)
text(ax, (c(0) + c(3)) / 2, 47, '3 kg = 3 000 g', 'resultat', 's')
arrow(ax, (c(5), 36.5), (c(3), 36.5), 'resultat', curve=0.5)
text(ax, c(4), 51, '100,07 cm = 1,0007 m', 'resultat', 's')
brace(ax, xs[0], xs[5] + w, 24, 'limite', 'kilo → centi : 5 pas, non montré')
save(fig, '11-048')
