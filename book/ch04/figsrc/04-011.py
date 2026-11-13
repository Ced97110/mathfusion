import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)

# colonne de gauche : 2 au carré
text(ax, 15, 64, '« 2 au carré »', 'autre', 's')
text(ax, 15, 57, '2²', 'autre', 'l')
for i in range(2):
    for j in range(2):
        box(ax, 8 + 7*i, 24 + 7*j, 7, 7, 'autre', lw=0.6, r=0)
text(ax, 15, 11, '2 × 2 = 4', 'autre', 'm')

# colonne du milieu : 2 au cube
text(ax, 44, 64, '« 2 au cube »', 'sujet', 's')
text(ax, 44, 57, '2³', 'sujet', 'l', weight='bold')
cubes(ax, [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)], (44, 18), 7, 'sujet')
text(ax, 44, 11, '2 × 2 × 2 = 8', 'sujet', 'm')

# colonne de droite : 2 multiplié par 3
text(ax, 73, 64, '2 multiplié par 3', 'limite', 's')
text(ax, 73, 57, "ce n'est pas 2³", 'limite', 'm')
for i in range(3):
    for j in range(2):
        box(ax, 64 + 6*i, 25 + 6*j, 6, 6, 'limite', lw=0.6, r=0)
text(ax, 73, 11, '2 × 3 = 6', 'limite', 'm')

text(ax, 44, 4, 'dans 2³, le 3 compte les 2', 'varie', 's')

save(fig, '04-011')
