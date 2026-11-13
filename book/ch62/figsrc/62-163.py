import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
assert math.factorial(3) == 6 and math.factorial(4) == 24
u, x0 = 2.9, 10
def bar(y, borne, plein, role):
    box(ax, x0, y, borne * u, 6, 'fixe', fill=False, dash=True, r=0.4, lw=0.8)
    box(ax, x0, y, plein * u, 6, role, r=0.4)
    for k in range(1, borne):
        line(ax, [(x0 + k * u, y), (x0 + k * u, y + 6)], 'fixe', lw=0.4)
# x^3 - 2 : borne 6, degré 6
text(ax, x0, 66, r'$x^3-2$', 'sujet', 'm', ha='left')
bar(54, 6, 6, 'varie')
text(ax, 32, 57, 'borne 3! = 6 :', 'encre', 's', ha='left')
text(ax, 32, 53, 'degré 6, atteinte', 'varie', 's', ha='left')
text(ax, x0, 47, 'étages 3 puis 2 : le maximum', 'encre', 's', ha='left')
# x^4 - 1 : borne 24, degré 2
text(ax, x0, 38, r'$x^4-1$', 'autre', 'm', ha='left')
bar(26, 24, 2, 'autre')
text(ax, x0, 21, 'degré 2', 'autre', 's', ha='left')
text(ax, x0 + 24 * u, 21, 'borne 4! = 24', 'encre', 's', ha='right')
text(ax, 44, 13, 'un seul étage : ajouter i ;', 'encre', 's')
text(ax, 44, 9, '−i, 1 et −1 sont déjà là', 'encre', 's')
save(fig, '62-163')
