import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'une base fixée, une base cible', 'encre', 's')
text(ax, 10, 52, 'départ', 'sujet', 's'); text(ax, 70, 52, 'arrivée', 'autre', 's')
for ox, role, a, b in [(10, 'sujet', 'e', 'f'), (62, 'autre', "e'", "f'")]:
    arrow(ax, (ox, 38), (ox + 12, 38), role); arrow(ax, (ox, 38), (ox, 50), role)
    text(ax, ox + 7, 34.5, a, role, 'm'); text(ax, ox - 3, 47, b, role, 'm')
arrow(ax, (28, 42), (56, 42), 'varie')
text(ax, 42, 46, 'une transformation', 'varie', 's')
for k in range(6):
    x = 8 + k * 12.5
    box(ax, x, 22, 11, 7, 'autre'); box(ax, x, 9, 11, 7, 'sujet')
    arrow(ax, (x + 5.5, 21.6), (x + 5.5, 16.4), 'varie', lw=0.7, both=True)
text(ax, 44, 32.5, '6 bases symplectiques', 'autre', 's'); text(ax, 44, 4.5, '6 transformations', 'sujet', 's')
save(fig, '75-118')
