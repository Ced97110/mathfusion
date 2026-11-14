import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$e=-0{,}1$ : produit $0{,}41>0$, somme $3{,}2>0$', 'varie', 's')
f = numberline(ax, 10, 66, 62, -1, 4, 1, labels=False, arrow_right=True)
text(ax, f(0), 56.5, '0', 'fixe', 's')
us = [3.066, 0.134]
for u in us:
    disc(ax, f(u), 62, 1.4, 'resultat')
text(ax, f(us[0]), 68, r'$u\approx3{,}07$', 'resultat', 's')
text(ax, f(us[1]) - 4, 68, r'$u\approx0{,}13$', 'resultat', 's')
text(ax, 77, 62, '$u$', 'fixe', 's')
g = numberline(ax, 10, 66, 20, -2, 2, 1, labels=False, arrow_right=True)
text(ax, g(0), 14.5, '0', 'fixe', 's')
for u in us:
    for sx in (-1, 1):
        disc(ax, g(sx * u ** 0.5), 20, 1.4, 'resultat')
        arrow(ax, (f(u), 59.5), (g(sx * u ** 0.5), 22.5), 'resultat', lw=0.6)
text(ax, g(-us[0] ** 0.5) + 1, 27, r'$-1{,}75$', 'resultat', 's')
text(ax, g(us[0] ** 0.5) - 1, 27, r'$1{,}75$', 'resultat', 's')
text(ax, g(-us[1] ** 0.5) - 3.5, 27, r'$-0{,}37$', 'resultat', 's')
text(ax, g(us[1] ** 0.5) + 3.5, 27, r'$0{,}37$', 'resultat', 's')
text(ax, 77, 20, '$x$', 'fixe', 's')
text(ax, 44, 6, '4 points communs', 'resultat', 'm')
save(fig, '70-114')
