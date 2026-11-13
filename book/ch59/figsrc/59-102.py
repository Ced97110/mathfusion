import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 22
f = numberline(ax, 8, 76, y, 0, 30, step=1, every=10, arrow_right=False)
for b in (0, 10, 20, 30):
    disc(ax, f(b), y + 7, 2.0, 'resultat')
    line(ax, [(f(b), y + 1.5), (f(b), y + 5)], 'resultat', lw=0.7)
disc(ax, f(7), y + 7, 2.0, 'limite')
line(ax, [(f(7), y + 1.5), (f(7), y + 5)], 'limite', lw=0.7)
text(ax, f(7), y - 4.5, '7', 'limite', 's')
text(ax, f(7) - 8, y + 14, '7·y₂ ≠ 0', 'limite', 's')
text(ax, f(20), y + 14, 'b·y₂ = 0', 'resultat', 's')
text(ax, 80, y - 4.5, 'b', 'fixe', 's')
brace(ax, f(0) - 2, f(30) + 2, y - 8.5, 'resultat', label='ann y₂ = (10) : multiples de 10', depth=2.0)
save(fig, '59-102')
