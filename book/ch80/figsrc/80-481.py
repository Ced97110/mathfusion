import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, a, b, op, inv, cap):
    box(ax, 6, y, 18, 10, 'sujet', label=a, size='l')
    box(ax, 64, y, 18, 10, 'resultat', label=b, size='l')
    arrow(ax, (25, y + 7), (63, y + 7), 'varie')
    arrow(ax, (63, y + 3), (25, y + 3), 'resultat')
    text(ax, 44, y + 9.8, op, 'varie', 's')
    text(ax, 44, y + 0.2, inv, 'resultat', 's')
    text(ax, 44, y + 14.5, cap, 'encre', 'm')
row(8, '5', '8', 'plus 3', 'moins 3', r'$5 + 3 = 8$ puis $8 - 3 = 5$')
row(40, '4', '12', r'fois 3', r'divisé par 3', r'$4 \times 3 = 12$ puis $12 \div 3 = 4$')
save(fig, '80-481')
