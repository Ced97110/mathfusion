import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$e_1\,e_2=x_1^2x_2+x_1x_2^2$', 'encre', 'l')
y, h, w = 28, 12, 22
xs = [3, 33, 63]
specs = [('sujet', r'$(1,\,0)$', 'plus haut\nde $e_1$', r'$x_1$'),
         ('autre', r'$(1,\,1)$', 'plus haut\nde $e_2$', r'$x_1x_2$'),
         ('resultat', r'$(2,\,1)$', 'plus haut\ndu produit', r'$x_1^2x_2$')]
for x, (role, lab, top, mon) in zip(xs, specs):
    box(ax, x, y, w, h, role, label=lab, size='m', weight='bold')
    text(ax, x + w / 2, y + h + 8, top, role, 's')
    text(ax, x + w / 2, y - 4.5, mon, role, 'm')
text(ax, 28.5, y + h / 2, '+', 'varie', 'xl', weight='bold')
text(ax, 58.5, y + h / 2, '=', 'varie', 'xl', weight='bold')
text(ax, 44, 8, r'les exposants s’additionnent', 'varie', 'm')
save(fig, '55-098')
