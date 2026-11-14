import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 18, 70, r'élément de $\mathbb{Q}(\sqrt{2})$', 'sujet', 's')
text(ax, 62, 70, 'polynôme de $\\mathbb{Q}[x]$', 'resultat', 's')
rows = [(r'$a\in\mathbb{Q}$', r'$x-a$ (degré 1)'),
        (r'$\sqrt{2}$', r'$x^2-2$ (degré 2)'),
        (r'$a+b\sqrt{2}$', 'degré 2 ou 1')]
for i, (el, pol) in enumerate(rows):
    y = 50 - i * 20
    box(ax, 3, y, 30, 12, 'sujet', label=el, size='s')
    arrow(ax, (33, y + 6), (46, y + 6), 'varie')
    box(ax, 46, y, 40, 12, 'resultat', label=pol, size='s')
text(ax, 44, 3, 'tous à racines distinctes', 'resultat', 's')
save(fig, '63-114')
