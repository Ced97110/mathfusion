import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
C = 8.2
def grid(x0, filled, role):
    for c in range(3):
        for r in range(2):
            on = (c, r) in filled
            box(ax, x0 + 9 * c, 46 - 9 * r, C, C, role if on else 'fixe', fill=on, r=0.3, lw=0.8 if on else 0.5)
        text(ax, x0 + 9 * c + C / 2, 57.5, str(c + 1), 'encre', 's')
    text(ax, x0 - 3.5, 46 + C / 2, 'a', 'encre', 's'); text(ax, x0 - 3.5, 37 + C / 2, 'b', 'encre', 's')
grid(12, {(0, 0), (1, 0), (2, 1)}, 'sujet'); grid(56, {(0, 0), (0, 1), (2, 1)}, 'autre')
box(ax, 2, 24, 40, 8, 'resultat', label='relation : oui', size='s'); box(ax, 2, 13, 40, 8, 'resultat', label='application : oui', size='s')
box(ax, 46, 24, 40, 8, 'resultat', label='relation : oui', size='s'); box(ax, 46, 13, 40, 8, 'limite', label='application : non', size='s')
save(fig, '42-262')
