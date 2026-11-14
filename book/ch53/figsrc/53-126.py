import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(104)
# p et q (secrets)
box(ax, 20, 88, 20, 10, 'autre', label='p = 5')
box(ax, 48, 88, 20, 10, 'autre', label='q = 11')
line(ax, [(30, 87.5), (30, 82), (58, 82), (58, 87.5)], 'fixe')
line(ax, [(44, 82), (44, 79)], 'fixe')
arrow(ax, (44, 79), (17, 74.5), 'varie'); arrow(ax, (44, 79), (71, 74.5), 'varie')
# n public, phi secret
box(ax, 2, 64, 30, 10, 'sujet', label='n = 55')
box(ax, 56, 64, 30, 10, 'autre', label='φ = 40')
# e public, d secret
box(ax, 2, 44, 30, 10, 'sujet', label='e = 3')
box(ax, 56, 44, 30, 10, 'autre', label='d = 27')
arrow(ax, (71, 63.5), (71, 54.5), 'varie')
arrow(ax, (32.5, 49), (55.5, 49), 'varie')
text(ax, 17, 38, 'clé publique : 55, 3', 'sujet', 's')
text(ax, 71, 38, 'clé privée : 27', 'autre', 's')
# message 8 -> 17 -> 8
box(ax, 2, 10, 20, 10, 'sujet', label='m = 8')
box(ax, 34, 10, 20, 10, 'varie', label='c = 17')
box(ax, 66, 10, 20, 10, 'resultat', label='m = 8')
arrow(ax, (23, 15), (33, 15), 'sujet'); arrow(ax, (55, 15), (65, 15), 'autre')
text(ax, 28, 23.5, 'puissance 3', 'sujet', 's')
text(ax, 60, 23.5, 'puissance 27', 'autre', 's')
save(fig, '53-126')
