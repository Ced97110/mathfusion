import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for g in range(4):
    gx = 8 + g * 20
    for k in range(3):
        disc(ax, gx + 2.3 + k * 5.5, 62, 2.3, 'sujet')
    brace(ax, gx, gx + 15.3, 58, 'resultat', '3')
text(ax, 44, 47, '12 ÷ 4 = 3 : tombe juste', 'resultat')
for i in range(3):
    box(ax, 5 + i * 17, 30, 14, 7, 'sujet')
text(ax, 69, 33.5, '÷ 4 = ?', 'limite', 'l')
text(ax, 29, 25, 'aucun entier', 'limite', 's')
arrow(ax, (29, 22), (29, 12), 'varie')
box(ax, 14, 3, 60, 8, 'varie', label='la fraction : nombre créé')
save(fig, '06-003')
