import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
text(ax, 36, 44, r'$A$', 'sujet', 'l')
text(ax, 31, 37.5, r'$e_1$', 'fixe', 'm'); text(ax, 40, 37.5, r'$e_2$', 'fixe', 'm')
rows = [((4, 6), 'sujet', r'$f_1$', r'$f_1=4e_1+6e_2$', 24), ((6, 4), 'autre', r'$f_2$', r'$f_2=6e_1+4e_2$', 12)]
for vals, role, name, eq, y in rows:
    text(ax, 22, y + 5, name, role, 'm')
    for j, v in enumerate(vals):
        box(ax, 26.5 + j * 9, y, 9, 10, role, label=str(v))
    arrow(ax, (45.5, y + 5), (51, y + 5), role)
    text(ax, 53, y + 5, eq, role, 'm', ha='left')
save(fig, '59-041')
