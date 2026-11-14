import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
# échelle : 1000 m = 25 mm
k = 25 / 1000
g = 10
h1, h2 = 1976 * k, 1925 * k
x1, x2, w = 12, 50, 18
box(ax, x1, g, w, h1, 'sujet')
box(ax, x2, g, w, h2, 'varie')
line(ax, [(x1, g + h1), (x2 + w + 8, g + h1)], 'fixe', dash=True, lw=0.7)
text(ax, x1 + w / 2, g + h1 / 2, r'$\beta=21{,}25°$', 'sujet', 's')
text(ax, x2 + w / 2, g + h2 / 2, r'$\beta=21{,}35°$', 'varie', 's')
text(ax, x1 + w / 2, g + h1 + 4, r'$h\approx1976$ m', 'sujet', 'm')
text(ax, x2 + w / 2, g - 4, r'$h\approx1925$ m', 'varie', 'm')
text(ax, x1 + w / 2, g - 4, 'angle lu', 'fixe', 's')
arrow(ax, (x1 + w + 2, g + 12), (x2 - 2, g + 12), 'varie')
text(ax, 40, g + 16, r'$+0{,}1°$', 'varie', 's')
arrow(ax, (x2 + w + 5, g + h1), (x2 + w + 5, g + h2), 'varie')
text(ax, 80, g + h1 - 2.6, r'$\approx51$ m', 'varie', 's')
text(ax, 80, g + h1 - 7.2, r'$(2{,}5\ \%)$', 'varie', 's')
text(ax, 44, 78, "0,1° d'erreur : 51 m d'écart", 'encre', 'm')
save(fig, '38-077')
