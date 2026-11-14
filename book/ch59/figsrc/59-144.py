import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 22, 58, 44, 11, 'sujet', label='théorème de structure')
arrow(ax, (32, 57.5), (22, 44), 'varie')
arrow(ax, (56, 57.5), (66, 44), 'varie')
# left: clock with 20 marks
cx, cy, r = 22, 31, 8.5
disc(ax, cx, cy, r, 'autre', fill=False)
for k in range(20):
    a = math.pi / 2 - 2 * math.pi * k / 20
    disc(ax, cx + r * math.cos(a), cy + r * math.sin(a), 0.7, 'autre')
text(ax, 22, 15, 'groupes abéliens finis', 'autre', 's')
text(ax, 22, 8, 'horloge à 20 heures', 'fixe', 's')
# right: quarter turn of a vector
ox, oy = 66, 31
line(ax, [(ox - 10, oy), (ox + 12, oy)], 'fixe', lw=0.5)
line(ax, [(ox, oy - 10), (ox, oy + 12)], 'fixe', lw=0.5)
arrow(ax, (ox, oy), (ox + 9, oy), 'sujet', lw=1.3)
arrow(ax, (ox, oy), (ox, oy + 9), 'varie', lw=1.3)
arrow(ax, (ox + 7, oy + 2.5), (ox + 2.5, oy + 7), 'varie', curve=0.3)
text(ax, 66, 15, 'transformations linéaires', 'sujet', 's')
text(ax, 66, 8, 'quart de tour', 'fixe', 's')
save(fig, '59-144')
