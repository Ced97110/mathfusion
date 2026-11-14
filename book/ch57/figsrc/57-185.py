import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 59, r'dans $\mathbb{Z}^2$', 'sujet', 's')
text(ax, 70, 59, r'dans $\mathbb{Z}$', 'resultat', 's')
text(ax, 46, 59, r'$\eta$ : $x-2y$', 'encre', 's')
rows = [(38, '(2;1) + (1;4) = (3;5)', '0 + (−7) = −7', 'la somme'),
        (12, '3 × (1;4) = (3;12)', '3 × (−7) = −21', 'le multiple')]
for y, a, b, c in rows:
    box(ax, 2, y, 38, 10, 'sujet', label=a, size='s')
    box(ax, 58, y, 28, 10, 'resultat', label=b, size='s')
    arrow(ax, (41, y + 5), (57, y + 5), 'varie', lw=1.2)
    text(ax, 49, y + 9, r'$\eta$', 'varie', 's')
    text(ax, 22, y - 4, c, 'encre', 's')
save(fig, '57-185')
