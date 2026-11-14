import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
for y, role, lab, d in ((34, 'sujet', '8 + 5 ; 9 ÷ 7', 'calcul, nombres connus'),
                        (20, 'autre', '8 + 5 = 13', 'phrase : vraie ou fausse'),
                        (6, 'fixe', r'$x+8$', 'une lettre : pas numérique')):
    box(ax, 3, y - 1, 32, 10, role, label=lab, weight='bold' if role == 'sujet' else 'normal')
    text(ax, 39, y + 4, d, role, 's', ha='left')
save(fig, '15-014')
