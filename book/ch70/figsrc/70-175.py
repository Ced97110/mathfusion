import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
left = [(50, 'sujet', 'coefficients b et c'), (36, 'fixe', 'suite de polynômes de Sturm'),
        (22, 'varie', 'signes : expressions en b, c'), (8, 'resultat', r'$b^2-4c\geq 0$')]
for y, role, s in left:
    box(ax, 2, y, 46, 9, role, label=s, size='s')
for y in (50, 36, 22): arrow(ax, (25, y), (25, y - 5), 'fixe')
right = [(50, 'sujet', r'$b=2,\ c=-3$'), (36, 'resultat', r'$b^2-4c=16\geq 0$'),
         (22, 'autre', r'$b=2,\ c=5$'), (8, 'limite', r'$b^2-4c=-16<0$')]
for y, role, s in right:
    box(ax, 54, y, 32, 9, role, label=s, size='s')
for y in (50, 22): arrow(ax, (70, y), (70, y - 5), 'fixe')
save(fig, '70-175')
