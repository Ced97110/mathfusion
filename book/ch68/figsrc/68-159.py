import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
text(ax, 44, 71, 'même syndrome 001', 'resultat', 'm')
rows = [('colonne 1', None, '001'), ('col. 2 + col. 3', '010', '011'),
        ('col. 4 + col. 5', '100', '101'), ('col. 6 + col. 7', '110', '111')]
for i, (lab, a, b) in enumerate(rows):
    y = 52 - i * 14
    text(ax, 2, y + 4, lab, 'encre', 's', ha='left')
    if a:
        box(ax, 26, y, 12, 8, 'sujet', label=a)
        text(ax, 42, y + 4, '+', 'encre', 'm')
    box(ax, 46, y, 12, 8, 'sujet', label=b)
    text(ax, 63, y + 4, '=', 'encre', 'm')
    box(ax, 68, y, 12, 8, 'resultat', label='001')
text(ax, 44, 4, '4 explications possibles', 'encre', 's')
save(fig, '68-159')
