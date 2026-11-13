import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 64, 61, 'la même lettre désigne :', 'encre', 'm')
box(ax, 4, 21, 22, 20, 'sujet', label=r'$M$', size='xl')
text(ax, 15, 14, 'ensemble non vide', 'sujet', 's')
for y, lab in [(50, 'ℕ : entiers naturels'), (31, '4 transformations'), (12, 'mots')]:
    box(ax, 44, y - 6, 40, 12, 'fixe', label=lab, size='m')
    arrow(ax, (27, 31), (43, y), 'varie')
save(fig, '44-055')
