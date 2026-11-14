import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
y = 30
f = numberline(ax, 6, 76, y, 0, 11, labels=False, arrow_right=False)
for v, r in [(0, 'fixe'), (5, 'fixe'), (7, 'sujet'), (10, 'fixe'), (11, 'varie')]:
    text(ax, f(v), y - 3.6, str(v), r, 's')
arrow(ax, (f(0), y + 1.5), (f(7), y + 1.5), 'sujet', curve=-0.4)
arrow(ax, (f(7), y + 1.5), (f(11), y + 1.5), 'varie', curve=-0.4)
text(ax, (f(0) + f(7)) / 2, y + 12.5, '7', 'sujet', 's')
text(ax, (f(7) + f(11)) / 2, y + 8.5, '+ 4', 'varie', 's')
text(ax, 44, y + 23, '7 + 4 = 11', 'encre', 'l')
yb = y - 8
brace(ax, f(0) + 0.5, f(5) - 0.5, yb, 'fixe', label='tour de 5')
brace(ax, f(5) + 0.5, f(10) - 0.5, yb, 'fixe', label='tour de 5')
brace(ax, f(10) + 0.5, f(11) - 0.5, yb, 'resultat', label='reste 1')
text(ax, 44, y - 22, '7 + 4 ≡ 1 (mod 5)', 'resultat', 'l')
save(fig, '44-146')
