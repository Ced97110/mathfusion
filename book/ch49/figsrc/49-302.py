import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 74, 'colorations du carré', 'sujet', 's')
text(ax, 66, 74, 'circuits à 3 entrées', 'autre', 's')
P = [(14, 52), (30, 52), (30, 66), (14, 66)]
poly(ax, P, 'fixe')
for i, p in enumerate(P):
    disc(ax, p[0], p[1], 2.8, 'sujet' if i % 2 == 0 else 'varie')
text(ax, 22, 44, 'à rotation près', 'sujet', 's')
for k in range(3):
    y = 55 + (k - 1) * 6
    line(ax, [(50, y), (60, y)], 'autre'); line(ax, [(72, y), (82, y)], 'autre')
box(ax, 60, 48, 12, 22, 'autre')
arrow(ax, (50, 49), (82, 49), 'varie', curve=0) if False else None
text(ax, 66, 44, 'à permutation près', 'autre', 's')
arrow(ax, (22, 38), (40, 24), 'resultat'); arrow(ax, (66, 38), (48, 24), 'resultat')
box(ax, 8, 4, 72, 19, 'resultat')
text(ax, 44, 16, 'le même calcul :', 'resultat', 'm')
text(ax, 44, 9, 'nombre d’orbites (Burnside)', 'resultat', 's')
save(fig, '49-302')
