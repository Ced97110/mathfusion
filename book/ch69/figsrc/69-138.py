import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$x^2-2$ a-t-il une racine ?', 'encre', 'm')
for x, lab, sub in [(24, '1', r'$x^2$'), (40, '0', r'$x$'), (56, '−2', 'constante')]:
    box(ax, x - 6, 56, 12, 10, 'sujet', label=lab)
text(ax, 44, 50, 'les trois coefficients', 'sujet', 's')
arrow(ax, (44, 47), (44, 41), 'varie')
box(ax, 10, 26, 68, 14, 'varie', label='calcul fini sur des signes')
arrow(ax, (44, 25), (44, 19), 'varie')
box(ax, 10, 3, 68, 15, 'resultat', label='oui ou non, sans construire\nla racine')
save(fig, '69-138')
