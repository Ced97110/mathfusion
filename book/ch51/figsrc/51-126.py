import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
xs = lambda k: 14 + 12 * (k - 1)
for k in range(1, 7):
    disc(ax, xs(k), 60, 3.5, 'sujet', label=str(k), size='m', lw=2.0 if k == 5 else 0.8)
    disc(ax, xs(k), 18, 3.5, 'resultat', label=str(k), size='m', lw=2.0 if k == 1 else 0.8)
for k in range(1, 7):
    r = (3 * k) % 7
    arrow(ax, (xs(k), 56.5), (xs(r), 21.5), 'resultat' if r == 1 else 'varie', lw=1.8 if r == 1 else 0.9)
text(ax, 44, 67.5, r'$\times 3$ dans ℤ/7 : départs 1 à 6', 'varie', 's'); text(ax, 44, 10, '6 places, chacune atteinte une fois', 'resultat', 's')
text(ax, 44, 3.5, r'$3\times5=1$ : 1 atteint, 5 = inverse', 'resultat', 's', weight='bold')
save(fig, '51-126')
