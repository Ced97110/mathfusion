import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 18, 54, 'relatif', 'sujet', 'm')
text(ax, 58, 54, 'rationnel a/b', 'resultat', 'm')
for yc, n in ((37, '−2'), (19, '5')):
    box(ax, 8, yc - 7, 20, 14, 'sujet', label=n, size='l')
    text(ax, 35, yc, '=', 'encre', 'l')
    box(ax, 42, yc - 7, 32, 14, 'resultat')
    text(ax, 58, yc + 3.5, n, 'sujet', 'm')
    line(ax, [(53, yc), (63, yc)], 'encre')
    text(ax, 58, yc - 3.5, '1', 'varie', 'm')
text(ax, 58, 6, 'bas = 1, et 1 ≠ 0', 'varie', 's')
save(fig, '12-077')
