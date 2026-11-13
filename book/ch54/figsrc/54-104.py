import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
assert 7 % 5 == 2 and 3 % 5 == 3
text(ax, 14, 51, 'anneau ℤ', 'fixe', 's')
text(ax, 74, 51, 'anneau ℤ/5', 'fixe', 's')
pairs = [(7, 2, 38), (3, 3, 16)]
for a, b, y in pairs:
    box(ax, 8, y, 12, 9, 'sujet', label=str(a), size='m')
    box(ax, 68, y, 12, 9, 'resultat', label=str(b), size='m')
    arrow(ax, (20, y + 4.5), (68, y + 4.5), 'varie')
    text(ax, 44, y + 8.5, rf'$\eta({a})={b}$', 'varie', 'm')
text(ax, 44, 4, r'$\eta$ : garder le reste modulo 5', 'varie', 's')
save(fig, '54-104')
