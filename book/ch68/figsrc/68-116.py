import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 22, 52, '$H$', 'sujet', 'm')
for c, v in enumerate([1, 1, 0]):
    box(ax, 30 + 10 * c, 48, 10, 8, 'limite' if c == 2 else 'sujet', label=str(v))
text(ax, 55, 40, 'colonne nulle', 'limite', 's')
box(ax, 2, 6, 84, 22, 'sujet', fill=False, dash=True)
box(ax, 5, 12, 28, 9, 'sujet', label='000 envoyé')
box(ax, 55, 12, 28, 9, 'varie', label='001 reçu')
arrow(ax, (33, 16.5), (55, 16.5), 'varie')
text(ax, 44, 24, 'erreur au bit 3', 'varie', 's')
save(fig, '68-116')
