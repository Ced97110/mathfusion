import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 26
f = numberline(ax, 6, 78, y, -3, 4, labels=False)
for v, r in ((-2, 'resultat'), (0, 'fixe'), (3, 'sujet')):
    text(ax, f(v), y - 3.6, f'${v}$', r)
disc(ax, f(3), y, 1.8, 'sujet')
disc(ax, f(-2), y, 1.8, 'resultat')
arrow(ax, (f(3) - 1, y + 3), (f(-2) + 1, y + 3), 'varie', curve=0.4)
text(ax, (f(3) + f(-2)) / 2, y + 12, '5 pas à gauche', 'varie', 's')
brace(ax, f(0), f(3), y - 7, 'sujet', '3 €')
brace(ax, f(-2), f(0), y - 7, 'resultat', 'dette : 2 €')
text(ax, 44, 55, r'$3-5=3+(-5)=-2$', 'encre', 'l')
save(fig, '13-068')
