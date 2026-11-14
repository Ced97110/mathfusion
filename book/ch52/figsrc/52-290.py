import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 48, 'Restes par 5 : le reste 3, cinq fois', 'encre', 'm')
w, g, x0, y = 10, 6, 7, 28
for i in range(5):
    x = x0 + i * (w + g)
    box(ax, x, y, w, 10, 'sujet', label='3', size='l')
    if i < 4: text(ax, x + w + g / 2, y + 5, '+', 'varie', 'l')
brace(ax, x0, x0 + 4 * (w + g) + w, y, 'varie', 'cinq additions')
arrow(ax, (44, 17), (44, 11), 'varie')
box(ax, 22, 1.5, 44, 9, 'resultat', label='15 : reste 0', size='m')
save(fig, '52-290')
