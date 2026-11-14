import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
for cx, name in ((22, 'Terre'), (66, 'Lune')):
    box(ax, cx - 18, 8, 36, 5, 'fixe')
    text(ax, cx, 3.5, name, 'fixe', 'm')
    for i in range(3):
        for j in range(2):
            box(ax, cx - 9 + i * 6, 15 + j * 6, 6, 6, 'sujet', r=0.4)
text(ax, 44, 52, 'quantité de matière', 'sujet', 'm', weight='bold')
text(ax, 44, 22, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 40, 'même masse', 'resultat', 'm')
save(fig, '11-050')
