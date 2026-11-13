import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'trois polynômes de départ', 'encre', 'm')
gens = [r'$x^2$', r'$y^2$', r'$xy$']
for i, g in enumerate(gens):
    box(ax, 12 + i * 24, 44, 16, 9, 'sujet', label=g)
# row 1 : x^3 y = x^2 * xy
def row(y, res, facs):
    box(ax, 3, y, 17, 9, 'resultat', label=res)
    text(ax, 24, y + 4.5, '$=$', 'encre')
    for i, f in enumerate(facs):
        box(ax, 29 + i * 20, y, 15, 9, 'sujet', label=f)
row(26, r'$x^3y$', [r'$x^2$', r'$xy$'])
row(8, r'$x^4y^2$', [r'$x^2$', r'$x^2$', r'$y^2$'])
save(fig, '56-063')
