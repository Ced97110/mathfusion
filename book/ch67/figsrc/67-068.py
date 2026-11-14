import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# x^4 - x has at most 4 roots ; in the field with 4 elements, the 4 elements are the 4 roots
box(ax, 22, 54, 44, 12, 'sujet', label=r'$x^4 - x$ : degré 4')
text(ax, 70, 49, 'racines', 'varie', 's')
E = ['0', '1', r'$\alpha$', r'$\alpha+1$']
for k, e in enumerate(E):
    x = 4 + k * 21
    box(ax, x, 18, 19, 22, 'fixe', fill=False, dash=True)
    box(ax, x + 2, 21, 15, 10, 'resultat', label=e, size='s')
    arrow(ax, (44, 53), (x + 9.5, 41.5), 'varie')
brace(ax, 4, 85, 16, 'resultat', label='4 éléments = 4 racines', size='s')
text(ax, 44, 4, 'au plus 4 places', 'fixe', 's')
save(fig, '67-068')
