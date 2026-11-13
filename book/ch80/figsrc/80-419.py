import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(58)
box(ax, 2, 38, 48, 18, 'sujet', label="A3\n$a\\vee(b\\wedge c)=$\n$(a\\vee b)\\wedge(a\\vee c)$", size='s')
box(ax, 2, 21, 48, 12, 'sujet', label=r"A4 : $a\vee O=a$", size='s')
box(ax, 2, 4, 48, 12, 'sujet', label=r"A5 : $a\vee a'=I$", size='s')
box(ax, 62, 24, 22, 12, 'varie', label=r"$a\vee a$", size='m')
for yc in (47, 27, 10): arrow(ax, (50, yc), (62, 30), 'varie')
arrow(ax, (73, 36), (73, 44), 'resultat')
box(ax, 62, 44, 22, 10, 'resultat', label=r"$=a$", size='m')
text(ax, 73, 17, 'jamais nommé', 'varie', 's')
save(fig, '80-419')
