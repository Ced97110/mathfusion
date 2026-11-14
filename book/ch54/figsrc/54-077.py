import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 16, 67, 'ℤ', 'sujet', 'l')
text(ax, 44, 67, 'reste mod 5', 'varie', 's')
text(ax, 72, 67, 'ℤ/5', 'resultat', 'l')
box(ax, 58, 10, 28, 52, 'resultat')
ys = [54, 42, 30, 18]
for y, a, b in zip(ys, ('1', '2', '5', '7'), ('1', '2', '0', '2')):
    box(ax, 8, y - 4.5, 16, 9, 'sujet', label=a)
    box(ax, 64, y - 4.5, 16, 9, 'encre', label=b)
    arrow(ax, (25, y), (63, y), 'varie')
text(ax, 72, 5, 'déjà un corps', 'resultat', 'm')
save(fig, '54-077')
