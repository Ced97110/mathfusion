import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cols = (52, 74)
text(ax, 3, 66, 'corps gauches', 'fixe', 's', ha='left')
text(ax, cols[0], 66, 'fini', 'encre', 's')
text(ax, cols[1], 66, 'commutatif', 'encre', 's', ha='center')
rows = (('cadran à 7', 1, 1), ('quatre tableaux', 1, 1), ('quaternions $\\mathbb{H}$', 0, 0))
for i, (lab, a, b) in enumerate(rows):
    y = 54 - i * 13
    text(ax, 3, y, lab, 'sujet', 's', ha='left')
    for x, v in zip(cols, (a, b)):
        box(ax, x - 8, y - 5, 16, 10, 'resultat' if v else 'limite', label='oui' if v else ('infini' if x == cols[0] else 'non'), size='s', r=0.6)
box(ax, 4, 4, 80, 11, 'resultat', label='corps gauche fini → commutatif', size='m')
save(fig, '51-284')
