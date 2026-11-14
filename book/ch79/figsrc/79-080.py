import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, 'un nombre avec lui-même', 'encre', 's')
for yy, tag, res, role in [(40, 'PPCM', '4', 'resultat'), (24, 'PGCD', '4', 'resultat'), (8, 'addition', '8', 'limite')]:
    text(ax, 2, yy + 5.5, tag, role, 's', ha='left')
    box(ax, 28, yy, 10, 11, 'sujet', label='4'); box(ax, 40, yy, 10, 11, 'sujet', label='4')
    arrow(ax, (52, yy + 5.5), (63, yy + 5.5), role)
    box(ax, 65, yy, 18, 11, role, label=res)
save(fig, '79-080')
