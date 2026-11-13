import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 24
f = numberline(ax, 8, 80, y, 10, 22, step=1, every=5, arrow_right=False)
# multiples de 5 : 10, 15, 20 ; a = 17
for v in (15, 20):
    disc(ax, f(v), y, 1.6, 'sujet')
disc(ax, f(17), y, 1.9, 'autre')
text(ax, f(17), y + 6, r'$a=17$', 'autre', 'm')
# couple 1 : q = 3, r = 2
arrow(ax, (f(15), y + 3), (f(17) - 1, y + 3), 'resultat', curve=-0.35)
text(ax, (f(15) + f(17)) / 2 - 6, y + 11, r'$q=3$, $r=2$', 'resultat', 's')
# couple 2 : q = 4, r = -3
arrow(ax, (f(20), y - 8.5), (f(17) + 1, y - 8.5), 'resultat', curve=-0.35)
text(ax, f(20) - 6, y - 14.5, r'$q=4$, $r=-3$', 'resultat', 's')
text(ax, 44, 55, r'$5\times 3=15$ et $5\times 4=20$ : multiples de $b=5$', 'sujet', 's')
text(ax, 44, 2.5, r'$|2|=2<5$ et $|-3|=3<5$ : deux couples', 'encre', 's')
save(fig, '56-123')
