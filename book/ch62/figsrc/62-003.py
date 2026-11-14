import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 10, 66, 22, -1, 2, step=1, labels=False, arrow_right=False)
for v in (-1, 0, 1, 2):
    text(ax, f(v), 25.5, f'{v}'.replace('-', '−'), 'fixe', 's')
pts = [(f(-1 + 0.05 * i), 22 + 4 * ((-1 + 0.05 * i) ** 3 - 2)) for i in range(0, 59)]
line(ax, pts, 'sujet', lw=1.2)
R = 2 ** (1 / 3)
disc(ax, f(R), 22, 1.4, 'resultat')
text(ax, 36, 36, '∛2 ≈ 1,26', 'resultat', 'm')
arrow(ax, (42.5, 34), (f(R) - 1.2, 23.6), 'resultat', lw=0.9)
text(ax, 70, 52, '$x^3-2$', 'sujet', 'l')
text(ax, 44, 4.5, 'les deux autres racines : pas sur cet axe', 'varie', 's')
text(ax, 20, 55, 'une seule racine réelle', 'resultat', 's')
save(fig, '62-003')
