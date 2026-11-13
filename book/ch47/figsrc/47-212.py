import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# row 1
box(ax, 2, 38, 24, 16, 'sujet'); text(ax, 14, 49, r'$\mathbb{Z}$', 'sujet', 'l'); text(ax, 14, 42, 'multiples de 12', 'sujet', 's')
arrow(ax, (27, 46), (46, 46), 'varie'); text(ax, 36.5, 50, 'regrouper', 'varie', 's')
for i in range(12):
    a = math.pi/2 - i*2*math.pi/12
    disc(ax, 68 + 11*math.cos(a), 46 + 11*math.sin(a), 2.2, 'resultat')
text(ax, 68, 46, '12', 'resultat', 'm')
# row 2
for k in range(2):
    box(ax, 3 + k*13, 8, 11, 17, 'sujet', fill=False, dash=True, r=1.5)
    for j in range(3): disc(ax, 8.5 + k*13, 11.5 + j*5, 2, 'sujet')
text(ax, 14, 28.5, r'$S_3$ : 6', 'sujet', 's')
arrow(ax, (32, 17), (50, 17), 'varie')
for k in range(2): disc(ax, 62 + k*14, 17, 4, 'resultat')
text(ax, 69, 8, r'$S_3/A_3$ : 2', 'resultat', 's')
text(ax, 44, 59, 'même geste, autre structure', 'encre', 's')
save(fig, '47-212')
