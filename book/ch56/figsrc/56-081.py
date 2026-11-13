import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
y = 38
f = numberline(ax, 6, 76, y, -12, 12, 1, every=3, arrow_right=True)
for v in range(-12, 13, 3):
    disc(ax, f(v), y, 1.7, 'sujet')
text(ax, 44, 60, '(3) : les multiples de 3', 'sujet', 'm', weight='bold')
arrow(ax, (f(3), y + 3), (f(9), y + 3), 'varie', curve=-0.5)
text(ax, f(6), y + 10, '$+6$', 'varie', 's')
text(ax, 44, 18, '$3+6=9$ : multiple de 3', 'resultat', 's')
text(ax, 44, 9, r'$3\times(-2)=-6$ : multiple de 3', 'resultat', 's')
save(fig, '56-081')
