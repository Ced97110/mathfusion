import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
y = 38
f = numberline(ax, 6, 78, y, 0, 180, step=45, arrow_right=False)
box(ax, f(0), y + 3, f(90) - f(0), 12, 'resultat', True, label='démontré par la figure\n(angles aigus)', size='s')
box(ax, f(90), y + 3, f(180) - f(90), 12, 'autre', True, label='admis ici\n(les autres cas)', size='s')
text(ax, f(135), y + 19, 'preuves : chapitres 39 et 41', 'autre', 's')
text(ax, 44, 68, r'$A+B$ en degrés', 'encre', 's')
arrow(ax, (f(105), y - 13), (f(105), y - 2), 'varie')
text(ax, f(105), y - 17, '60° + 45° = 105° : cas admis', 'varie', 's')
text(ax, f(105), y - 24, 'formule = calculatrice = 0,9659', 'varie', 's')
text(ax, f(105), y - 30, 'un cas qui réussit ne prouve pas', 'varie', 's')
save(fig, '34-080')
