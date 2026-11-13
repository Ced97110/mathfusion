import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0 = 4
for i in range(3):
    for j in range(4):
        box(ax, x0 + i * 28 + j * 6, 46, 6, 8, 'sujet', r=0.3)
text(ax, 44, 59, '3 tablettes coupées en 4', 'sujet')
arrow(ax, (44, 44), (44, 34), 'varie')
text(ax, 50, 39, '12 morceaux', 'varie', ha='left')
for g in range(4):
    gx = 5 + g * 21
    for k in range(3):
        box(ax, gx + k * 5, 20, 5, 6, 'resultat', r=0.3)
    brace(ax, gx, gx + 15, 20, 'resultat', '3')
text(ax, 44, 6, '4 personnes : 3 chacune', 'encre')
save(fig, '06-002')
