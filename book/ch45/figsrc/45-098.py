import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 24
line(ax, [(8, y), (80, y)], 'fixe', lw=1.2)
xs = [10, 44, 78]
for x in xs: disc(ax, x, y, 2.2, 'sujet')
text(ax, xs[0], y + 9, '1821', 'sujet', 'l', weight='bold'); text(ax, xs[0], y + 4.5, 'naissance', 'encre', 's')
text(ax, xs[0], y - 7, 'Angleterre', 'encre', 's')
text(ax, xs[2], y + 9, '1863', 'sujet', 'l', weight='bold'); text(ax, xs[2], y + 4.5, 'professeur', 'encre', 's')
text(ax, xs[2], y - 7, 'Cambridge', 'encre', 's')
box(ax, 22, y - 12, 44, 8, 'varie', label='14 ans avocat')
text(ax, 44, y + 9, 'plus de 300 articles', 'varie', 's')
text(ax, 44, y - 18, 'de mathématiques', 'varie', 's')
save(fig, '45-098')
