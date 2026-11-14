import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
w, h = 5, 6
def word(y, bits, role):
    for i, b in enumerate(bits):
        box(ax, 2 + i * w, y, w, h, role, label=b)
word(54, '1100101', 'sujet')
text(ax, 42, 57, r'$1 + x + x^4 + x^6$', 'sujet', 's', ha='left')
word(42, '1000001', 'autre')
text(ax, 42, 45, r'$1 + x^6$', 'autre', 's', ha='left')
text(ax, 39, 50, '+', 'encre', 'm')
line(ax, [(2, 37), (86, 37)], 'fixe')
word(26, '0100100', 'resultat')
text(ax, 42, 29, r'$x + x^4$', 'resultat', 's', ha='left')
text(ax, 44, 16, r'$1$ et $x^6$ s’annulent', 'varie', 's')
text(ax, 44, 7, r'$1 + 1 = 0$', 'varie', 's')
save(fig, '68-178')
