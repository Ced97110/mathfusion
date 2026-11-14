import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, 'parties de 4 sommets : 16', 'sujet', 's')
counts = [1, 4, 6, 4, 1]
xs = [14, 29, 44, 59, 74]
for k, (x, c) in enumerate(zip(xs, counts)):
    text(ax, x, 60, str(k), 'encre', 'm')
    for j in range(c):
        disc(ax, x, 50 - j * 6, 2.4, 'sujet')
text(ax, 44, 11, 'taille = nombre de sommets', 'encre', 's')
arrow(ax, (xs[1] + 2.5, 50), (xs[1] + 2.5, 38), 'varie', curve=-0.5)
text(ax, xs[1] + 9, 44, r'$r$', 'varie', 's')
text(ax, 44, 4.5, 'la taille ne change pas', 'varie', 's')
save(fig, '49-123')
