import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
bits = '1100101'
w, h, x0 = 9, 7, 12
text(ax, 44, 57, 'mot 1100101, bits numérotés dès 0', 'encre', 's')
for i, b in enumerate(bits):
    box(ax, x0 + i * w, 30, w, h, 'sujet' if b == '1' else 'fixe', label=b)
    text(ax, x0 + (i + 0.5) * w, 42, rf'$x^{{{i}}}$', 'varie', 's')
    text(ax, x0 + (i + 0.5) * w, 25, str(i), 'fixe', 's')
text(ax, 6, 25, 'n°', 'fixe', 's')
text(ax, 44, 15, r'$1 + x + x^4 + x^6$', 'resultat', 'l')
text(ax, 44, 5, r'le bit $i$ est le coefficient de $x^i$', 'encre', 's')
save(fig, '68-177')
