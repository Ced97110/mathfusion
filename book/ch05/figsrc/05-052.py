import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'avec la méthode : 4 essais pour 47', 'varie', 'm')
for x, p in zip([4, 18, 32, 46], [2, 3, 5, 7]):
    box(ax, x, 44, 10, 9, 'varie', label=str(p), size='l')
for x in [14.4, 28.4, 42.4]:
    arrow(ax, (x, 48.5), (x + 3.2, 48.5), 'varie', lw=0.8)
arrow(ax, (56.4, 48.5), (59.6, 48.5), 'resultat', lw=0.8)
box(ax, 60, 42, 26, 13, 'resultat')
text(ax, 73, 50.5, r'quotient $6 < 7$', 'resultat', 's')
text(ax, 73, 46, 'on arrête', 'resultat', 's')
text(ax, 44, 33, 'sans la méthode : 45 essais, de 2 à 46', 'fixe', 'm')
c = 5.0
x0 = (88 - 15 * c) / 2
for k in range(45):
    i, j = k % 15, k // 15
    box(ax, x0 + i * c, 24 - j * c - 5 + 4, c, c, 'fixe', r=0.3, lw=0.6)
save(fig, '05-052')
