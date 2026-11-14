import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(84)
w, h, x0 = 7, 6.5, 22
text(ax, 44, 80, 'colonnes de H', 'encre', 's')
for i in range(1, 8):
    text(ax, x0 + (i - 0.5) * w, 74, str(i), 'fixe', 's')
for r, name in enumerate('ABC'):
    y = 61 - r * h
    text(ax, 17, y + h / 2, name, 'encre', 's')
    for i in range(1, 8):
        bit = (i >> (2 - r)) & 1
        box(ax, x0 + (i - 1) * w, y, w, h, 'sujet' if i == 6 else 'fixe', label=str(bit))
cx = x0 + 5.5 * w
text(ax, cx - 3, 43, 'syndrome 110 = colonne 6', 'resultat', 's', ha='right')
def word(y, bits, roles):
    for i, b in enumerate(bits):
        box(ax, x0 + i * w, y, w, h, roles[i], label=b)
text(ax, 17, 33, 'reçu', 'encre', 's', ha='right')
word(30, '0011011', ['fixe'] * 5 + ['varie', 'fixe'])
arrow(ax, (cx, 48.5), (cx, 37.5), 'resultat')
arrow(ax, (cx, 29), (cx, 16.5), 'varie')
text(ax, cx + 3, 22.5, 'inverser le bit 6', 'varie', 's', ha='left')
text(ax, 17, 11, 'corrigé', 'encre', 's', ha='right')
word(8, '0011001', ['resultat'] * 7)
save(fig, '68-158')
