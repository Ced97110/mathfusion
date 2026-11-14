import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'x⁵ − 1 = (x − 1)(x⁴ + x³ + x² + x + 1)', 'sujet', 's', weight='bold')
rows = [(34, '2⁵ − 1 = 31', '2 − 1 = 1', '16+8+4+2+1 = 31'),
        (14, '3⁵ − 1 = 242', '3 − 1 = 2', '81+27+9+3+1 = 121')]
for y, a, b, c in rows:
    box(ax, 2, y, 26, 11, role='sujet', label=a)
    text(ax, 31, y + 5.5, '=', 'resultat', 'l')
    box(ax, 34, y, 18, 11, role='varie', label=b, size='s')
    text(ax, 55, y + 5.5, '×', 'encre', 'l')
    box(ax, 58, y, 28, 11, role='autre', label=c, size='s')
text(ax, 44, 4, 'x = 2 puis x = 3 : même forme', 'encre', 's')
save(fig, '63-157')
