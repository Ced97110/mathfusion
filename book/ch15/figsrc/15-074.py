import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 71, 'convention', 'resultat', 'm')
for i, (lab, d) in enumerate([(r'$9x^{2}$', 'degré 2'), (r'$-50x$', 'degré 1'), (r'$-13$', 'constante')]):
    box(ax, 4 + i * 28, 52, 26, 11, 'sujet', label=lab, size='m')
    text(ax, 17 + i * 28, 46, d, 'sujet', 's')
arrow(ax, (6, 38), (82, 38), 'varie')
text(ax, 44, 33, 'degrés qui diminuent', 'varie', 's')
text(ax, 44, 22, 'autre ordre, même polynôme :', 'fixe', 's')
box(ax, 8, 6, 72, 10, 'fixe', dash=True, label=r'$-50x+9x^{2}-13$', size='m')
save(fig, '15-074')
