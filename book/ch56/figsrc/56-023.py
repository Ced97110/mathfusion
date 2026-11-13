import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 96, 'intégrité ⇒ simplification', 'sujet', 'm')
steps = ['3b = 3c', '3(b − c) = 0', 'b − c = 0', 'b = c']
notes = ['tout à gauche', '3 ≠ 0 et intégrité', 'on ajoute c']
for i, s in enumerate(steps):
    y = 82 - i * 14
    box(ax, 4, y, 40, 9, 'resultat' if i == 3 else 'sujet', label=s)
    if i < 3:
        arrow(ax, (24, y), (24, y - 5), 'varie')
        text(ax, 48, y - 2.5, notes[i], 'varie', 's', ha='left')
text(ax, 44, 30, 'simplification ⇒ intégrité', 'autre', 'm')
box(ax, 4, 16, 40, 9, 'autre', label='3b = 0 = 3 × 0')
arrow(ax, (24, 16), (24, 11), 'varie')
text(ax, 48, 13.5, 'on simplifie par 3', 'varie', 's', ha='left')
box(ax, 4, 2, 40, 9, 'resultat', label='b = 0')
save(fig, '56-023')
