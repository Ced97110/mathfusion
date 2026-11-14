import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
rows = [(40, 'fixe', r'$y-3=16$', 'égal, mais pas de racine'), (24, 'fixe', r'$\sqrt{y-3}$', "racine, mais pas d'égal"),
        (8, 'sujet', r'$\sqrt{y-3}=4$', 'racine ET égal : à résoudre')]
for y, role, e, tag in rows:
    box(ax, 3, y, 34, 11, role, label=e)
    text(ax, 42, y + 5.5, tag, role, 's', ha='left')
save(fig, '22-106')
