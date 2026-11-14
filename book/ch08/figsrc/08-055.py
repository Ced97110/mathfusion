import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
c = [18, 30, 42, 58]
text(ax, 8, 76, '114,1', 'sujet', 'm', ha='left') if False else None
for x, d in zip(c, '1141'):
    box(ax, x - 5, 62, 10, 11, 'sujet', label=d, size='l')
text(ax, 50, 66, ',', 'sujet', 'xl', weight='bold')
text(ax, 76, 67.5, r'$\div\,7$', 'varie', 'l', weight='bold')
for x, d in zip(c[1:], '163'):
    box(ax, x - 5, 30, 10, 11, 'resultat', label=d, size='l')
text(ax, 50, 34, ',', 'resultat', 'xl', weight='bold')
line(ax, [(50, 61), (50, 43)], 'varie', dash=True); arrow(ax, (50, 45), (50, 43), 'varie')
text(ax, 54, 52, 'même place', 'varie', 's', ha='left')
text(ax, 58, 22, 'dixièmes', 'resultat', 's')
text(ax, 8, 12, r'$114\div7=16$, reste 2', 'fixe', 's', ha='left')
text(ax, 8, 4, r'on abaisse 1 : $21\div7=3$', 'fixe', 's', ha='left')
save(fig, '08-055')
