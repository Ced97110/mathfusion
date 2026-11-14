import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
y = 26
f = numberline(ax, 8, 70, y, -13, 13, labels=False)
line(ax, [(f(0), y + 1.5), (f(0), y + 16)], 'fixe', dash=True)
for v, r in ((-12, 'sujet'), (0, 'fixe'), (12, 'resultat')):
    text(ax, f(v), y - 3.6, f'${v}$', r)
disc(ax, f(-12), y, 1.8, 'sujet')
disc(ax, f(12), y, 1.8, 'resultat')
arrow(ax, (f(-12) + 1, y + 3), (f(12) - 1, y + 3), 'varie', curve=-0.45)
text(ax, f(0), y + 21, 'les deux signes se retournent', 'varie', 's')
text(ax, f(-12), y - 9.5, 'dette de 12 €', 'sujet', 's')
text(ax, f(12) - 4, y - 9.5, '12 € de plus', 'resultat', 's')
text(ax, 44, 4, r'$-(-12)=12$', 'encre', 'l')
save(fig, '13-070')
