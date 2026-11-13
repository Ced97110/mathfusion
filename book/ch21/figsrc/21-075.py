import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, r'commun à 4 et à 6', 'encre', 'm')
f = numberline(ax, 8, 80, 22, 0, 36, 6, labels=False, arrow_right=False)
for v, r in [(6, 'limite'), (12, 'resultat'), (24, 'resultat'), (36, 'resultat')]:
    disc(ax, f(v), 31, 3.6, r, label=str(v), size='s', lw=1.6 if v == 12 else 0.8)
text(ax, f(6), 14, 'ne marche pas', 'limite', 's')
arrow(ax, (f(12) + 6, 41), (f(12) + 1.5, 35), 'varie'); text(ax, f(12) + 12, 43, 'le plus petit', 'resultat', 's')
save(fig, '21-075')
