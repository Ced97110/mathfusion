import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
box(ax, 4, 86, 80, 9, 'fixe', True, r'bas gardé : $2y-5$', 's')
rows = [(70, 'sujet', r'$5y+3-(2y+4)$', 'haut avec parenthèse'),
        (50, 'varie', r'$5y+3-2y-4$', 'signes changés'),
        (30, 'resultat', r'$3y-1$', 'on regroupe')]
for y, role, expr, lab in rows:
    box(ax, 4, y, 46, 10, role, True, expr)
    text(ax, 54, y + 5, lab, role, 's', ha='left')
arrow(ax, (27, 70), (27, 61), 'varie'); arrow(ax, (27, 50), (27, 41), 'varie')
box(ax, 4, 4, 38, 10, 'autre', True, r'$y=3$ : $18-10=8$', 's')
box(ax, 46, 4, 38, 10, 'autre', True, r'$3y-1=8$', 's')
text(ax, 44, 9, r'$=$', 'resultat', 'l')
text(ax, 44, 22, 'contrôle avec y = 3', 'autre', 's')
save(fig, '21-083')
