import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 20
f = numberline(ax, 6, 78, y, -16, 1, labels=False)
for v in (0, -5, -10, -15):
    text(ax, f(v), y - 3.6, f'${v}$', 'resultat' if v == -15 else 'fixe')
disc(ax, f(-15), y, 1.8, 'resultat')
for a in (0, -5, -10):
    arrow(ax, (f(a) - 0.8, y + 2.5), (f(a - 5) + 0.8, y + 2.5), 'varie', curve=0.7)
    text(ax, f(a - 2.5), y + 12, r'$-5$', 'varie', 's')
text(ax, 44, 45, r'$3\times(-5)=-15$', 'encre', 'l')
text(ax, 44, 4, 'à gauche de 0 : négatif', 'resultat', 's')
save(fig, '13-072')
