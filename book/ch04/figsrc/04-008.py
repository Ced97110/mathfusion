import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)

# le signe c
box(ax, 38, 54, 12, 10, 'sujet')
text(ax, 44, 59, 'c', 'sujet', 'l', style='italic', weight='bold')
text(ax, 52, 59, 'longueur du côté', 'sujet', 'm', ha='left')

# trois figures grises
for i in range(3):
    for j in range(3):
        box(ax, 5 + 5*i, 14 + 5*j, 5, 5, 'fixe', lw=0.6, r=0)
for i in range(5):
    for j in range(5):
        box(ax, 27 + 5*i, 14 + 5*j, 5, 5, 'fixe', lw=0.6, r=0)
cubes(ax, [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)], (75, 14), 5.5, 'fixe')

# le même nom c sur le côté de chaque figure
line(ax, [(5, 29), (20, 29)], 'sujet', lw=1.6)
line(ax, [(27, 39), (52, 39)], 'sujet', lw=1.6)
C0 = (75, 14)
line(ax, [iso(0, 2, 0, C0, 5.5), iso(0, 2, 2, C0, 5.5)], 'sujet', lw=1.6)
text(ax, 12.5, 32, 'c', 'sujet', 'm', style='italic')
text(ax, 39.5, 42, 'c', 'sujet', 'm', style='italic')
text(ax, 62.5, 25, 'c', 'sujet', 'm', style='italic')
for tip in ((12.5, 34), (39.5, 44), (63, 27.5)):
    line(ax, [(44, 54), tip], 'sujet', lw=0.5, dash=True)

# valeur de c et résultat
text(ax, 12.5, 10, 'c = 3', 'varie', 'm')
text(ax, 39.5, 10, 'c = 5', 'varie', 'm')
text(ax, 75, 10, 'c = 2', 'varie', 'm')
text(ax, 12.5, 4.5, '9 carreaux', 'resultat', 's')
text(ax, 39.5, 4.5, '25 carreaux', 'resultat', 's')
text(ax, 75, 4.5, '8 cubes', 'resultat', 's')

save(fig, '04-008')
