import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
u = 8.0; ox, oy = 5.0, 24.0
P = lambda x, y: (ox + x * u, oy + y * u)
for x in range(0, 11, 2):
    ax.add_patch(Rectangle((P(x, 0)[0] - 2.6, oy - 3), 5.2, 9 * u + 6, fc=FILL['sujet'], ec='none', alpha=0.9, zorder=0.5))
for y in (0, 3, 6, 9):
    ax.add_patch(Rectangle((ox - 3, P(0, y)[1] - 2.6), 10 * u + 6, 5.2, fc=FILL['autre'], ec='none', alpha=0.7, zorder=0.6))
for i in range(0, 11):
    for j in range(0, 10):
        if i % 2 == 0 and j % 3 == 0:
            disc(ax, *P(i, j), 1.0, 'resultat')
        else:
            disc(ax, *P(i, j), 0.4, 'fixe')
text(ax, P(2, 3)[0] + 2.5, P(2, 3)[1] - 4.5, r'$(2\,;\,3)$', 'resultat', 's')
text(ax, P(4, 6)[0] + 2.5, P(4, 6)[1] - 4.5, r'$(4\,;\,6)$', 'resultat', 's')
text(ax, P(6, 9)[0] + 4, P(6, 9)[1] - 4.5, r'$(6\,;\,9)=(2\,;\,3)+(4\,;\,6)$', 'resultat', 's', ha='right')
box(ax, 2, 11, 41, 8, 'sujet', label=r'$N_1$ : 1er nombre pair', size='s')
box(ax, 45, 11, 41, 8, 'autre', label=r'$N_2$ : 2e multiple de 3', size='s')
disc(ax, 8, 5, 1.0, 'resultat')
text(ax, 13, 5, r'$N_1\cap N_2$ : les deux à la fois', 'resultat', 's', ha='left')
save(fig, '57-134')
