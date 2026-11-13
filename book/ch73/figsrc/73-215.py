import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(52, '(1, 0, 0)', r'$Q=1$'), (38, '(1, 1, 0)', r'$Q=2$'), (24, '(1, 2, 2)', r'$Q=9$')]
for y, v, q in rows:
    box(ax, 3, y, 24, 9, 'sujet', label=v, size='s')
    arrow(ax, (27, y + 4.5), (34, y + 4.5), 'varie')
    box(ax, 34, y, 16, 9, 'resultat', label=q, size='s')
    arrow(ax, (50, y + 4.5), (58, y + 4.5), 'fixe')
box(ax, 58, 24, 27, 37, 'resultat', label='valeurs\npositives :\ndes carrés\ndans $\\mathbb{R}$', size='s')
text(ax, 44, 14, r'$2\times 1=2=(\sqrt{2})^2$', 'encre', 'm')
text(ax, 44, 6, r'2 est un carré dans $\mathbb{R}$', 'resultat', 's')
save(fig, '73-215')
