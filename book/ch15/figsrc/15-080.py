import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'on coupe aux signes', 'varie', 's')
items = [(r'$9x^{2}$', 'coeff. 9', 'degré 2'), (r'$-50x$', 'coeff. −50', 'degré 1'), (r'$-13$', 'constante', 'sans lettre')]
for i, (l, c, d) in enumerate(items):
    x = 3 + i * 29
    box(ax, x, 52, 26, 12, 'sujet', label=l, size='m')
    text(ax, x + 13, 45, c, 'sujet', 's'); text(ax, x + 13, 39, d, 'fixe' if i else 'resultat', 's')
    arrow(ax, (x + 13, 69), (x + 13, 65), 'varie') if False else None
box(ax, 8, 6, 72, 17, 'resultat')
text(ax, 44, 17, '3 termes · degré 2', 'resultat', 'm'); text(ax, 44, 11, 'trinôme quadratique', 'resultat', 'm')
save(fig, '15-080')
