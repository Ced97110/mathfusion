import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 10, 23, 68, 14, 'sujet')
labs = ['$e$', '$r$', '$r^2$']
for i, x in enumerate([24, 44, 64]):
    disc(ax, x, 30, 4.8, 'sujet', label=labs[i])
for i, (x, l) in enumerate(zip([24, 44, 64], [r'$s$', r'$sr$', r'$sr^2$'])):
    disc(ax, x, 12, 4.8, 'fixe', label=l)
text(ax, 24, 42, r"$G'$ : les 3 rotations", 'sujet', 's')
text(ax, 66, 53, r'un commutateur : $r^2$', 'varie', 's')
arrow(ax, (64, 51), (64, 35.2), 'varie')
text(ax, 44, 3, 'hors $G\'$ : 3 réflexions', 'fixe', 's')
save(fig, '50-211')
