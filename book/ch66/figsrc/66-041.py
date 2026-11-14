import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 57, r'6 objets en groupes de 3', 'resultat', 'm')
text(ax, 66, 57, r'6 objets en groupes de 4', 'limite', 'm')
# left: two groups of three
for g in range(2):
    y0 = 38 - g * 13
    box(ax, 4, y0 - 6, 36, 12, 'resultat', fill=False, dash=True)
    for k in range(3):
        disc(ax, 10 + k * 12, y0, 3.5, 'sujet')
text(ax, 22, 15, r'2 groupes, reste 0', 'resultat', 'm')
box(ax, 8, 3, 28, 9, 'resultat', label=r'$3 \mid 6$ : vrai')
# right: one group of four then 2 left over
box(ax, 48, 30, 36, 12, 'limite', fill=False, dash=True)
for k in range(4):
    disc(ax, 53 + k * 8.5, 36, 3.2, 'sujet')
for k in range(2):
    disc(ax, 53 + k * 8.5, 22, 3.2, 'varie')
text(ax, 66, 15, r'reste 2', 'varie', 'm')
box(ax, 52, 3, 28, 9, 'limite', label=r'$4 \nmid 6$ : faux')
save(fig, '66-041')
