import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

p = 2
c6 = 3 * p
c = c6 + 7
assert (c6, c) == (6, 13) and 3 * 9 == 27 == 26 + 1
back6 = c - 7
prod = 9 * back6
assert back6 == 6 and prod == 54 and prod % 26 == p

fig, ax = canvas(58)
xs = [4, 38, 72]
w, h = 12, 12
text(ax, 44, 55, r'chiffrer : $\times\,3$, puis $+\,7$', 'sujet', 'm')
for x, lab in zip(xs, ['2', '6', '13']):
    box(ax, x, 34, w, h, 'sujet', label=lab)
arrow(ax, (xs[0] + w + 1, 40), (xs[1] - 1, 40), 'sujet')
arrow(ax, (xs[1] + w + 1, 40), (xs[2] - 1, 40), 'sujet')
text(ax, 27, 44, r'$\times\,3$', 'sujet', 'm')
text(ax, 61, 44, r'$+\,7$', 'sujet', 'm')
text(ax, 44, 27, r'déchiffrer : $-\,7$, puis $\times\,9$', 'resultat', 'm')
for x, lab in zip(xs, ['54 → 2', '6', '13']):
    box(ax, x, 6, w, h, 'resultat', label=lab, size='s')
arrow(ax, (xs[2] - 1, 12), (xs[1] + w + 1, 12), 'resultat')
arrow(ax, (xs[1] - 1, 12), (xs[0] + w + 1, 12), 'resultat')
text(ax, 61, 16, r'$-\,7$', 'resultat', 'm')
text(ax, 27, 16, r'$\times\,9 = 54$', 'resultat', 'm')
text(ax, 44, 1.5, r'$9 = 3^{-1}$ car $3 \times 9 = 27 = 26 + 1$', 'fixe', 's')
save(fig, '53-057')
