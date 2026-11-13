import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 24
f = numberline(ax, 6, 78, y, -5, 11, labels=False)
for v, r in ((-3, 'sujet'), (0, 'fixe'), (9, 'resultat')):
    text(ax, f(v), y - 3.6, f'${v}$', r)
disc(ax, f(-3), y, 1.8, 'sujet')
disc(ax, f(9), y, 1.8, 'resultat')
arrow(ax, (f(-3) + 1, y + 3), (f(9) - 1, y + 3), 'varie', curve=-0.3)
text(ax, f(3), y + 13, '12 pas à droite', 'varie', 's')
text(ax, 44, 48, r'$-3-(-12)=-3+12=9$', 'encre', 'l')
text(ax, 44, 6, 'soustraire $-12$ : aller à droite', 'varie', 's')
save(fig, '13-069')
