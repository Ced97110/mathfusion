import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
w, h = 4.4, 6
def word(x0, y, bits, roles):
    for i, b in enumerate(bits):
        box(ax, x0 + i * w, y, w, h, roles[i], label=b)
cases = [(50, '0011001', '0011011'), (22, '1110000', '1110010')]
for y, c, r in cases:
    word(2, y, c, ['fixe'] * 7)
    word(48, y, r, ['sujet'] * 5 + ['varie'] + ['sujet'])
    arrow(ax, (34, y + 3), (46, y + 3), 'varie')
    text(ax, 40, y + 7.5, r'$+\, e$', 'varie', 's')
    text(ax, 48 + 3.5 * w, y - 4.5, r'$Hr$ = 110', 'resultat', 'm')
text(ax, 17, 60, r'$c$ envoyé', 'encre', 's')
text(ax, 63, 60, r'$r$ reçu', 'encre', 's')
text(ax, 44, 36, r'même erreur $e$ = 0000010', 'varie', 's')
text(ax, 44, 4, 'même erreur, même syndrome', 'resultat', 's')
save(fig, '68-156')
