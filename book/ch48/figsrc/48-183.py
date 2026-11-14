import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 44, 69, 'les entiers', 'sujet', 's')
for i, v in enumerate(range(-2, 3)):
    x = 14 + i * 15
    disc(ax, x, 56, 3.3, 'sujet', label=str(v), size='s')
    arrow(ax, (x, 52.6), (44 + (x - 44) * 0.12, 27), 'varie', lw=0.8)
disc(ax, 44, 20, 6.5, 'resultat')
line(ax, [(44, 20), (50.5, 20)], 'resultat')
text(ax, 44, 8, 'rotation de 0°', 'resultat', 's')
text(ax, 86, 38, 'tous au même endroit', 'varie', 's', ha='right')
text(ax, 4, 20, 'rien retenu', 'limite', 's', ha='left')
save(fig, '48-183')
