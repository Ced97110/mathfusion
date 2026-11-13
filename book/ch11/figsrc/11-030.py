import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
eq = ['1 pied = 12 po', '1 yard = 3 pieds', '1 mile = 5 280 pieds', '1 livre = 16 onces', '1 gallon = 4 quarts', '1 h = 60 min']
for k, t in enumerate(eq):
    r, c = divmod(k, 2)
    box(ax, 3 + c * 43, 44 - r * 11, 40, 8.5, 'autre', label=t, size='s')
text(ax, 44, 56, 'six égalités', 'autre', 'm', weight='bold')
text(ax, 44, 9, '12 ne donne ni 3 ni 5 280', 'limite', 's')
text(ax, 44, 17, 'à retenir une par une', 'limite', 's')
save(fig, '11-030')
