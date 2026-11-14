import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
c, x0, y0 = 8.5, 14, 6
odd = {1, 3, 5, 7}
for r in range(8):
    for k in range(8):
        y = y0 + (7 - r) * c
        if r == k and r in odd:
            box(ax, x0 + k * c, y, c, c, 'resultat', label='1', r=0.2, size='s')
        else:
            box(ax, x0 + k * c, y, c, c, 'sujet' if r in odd else 'fixe', r=0.2)
for v in (1, 3, 5, 7):
    text(ax, x0 + v * c + c / 2, y0 + 8 * c + 2.5, str(v), 'sujet', 's')
    text(ax, x0 - 3, y0 + (7 - v) * c + c / 2, str(v), 'sujet', 's')
text(ax, x0 + 4 * c, y0 + 8 * c + 8, 'produits modulo 8 : le 1 en vert', 'resultat', 's')
save(fig, '44-165')
