import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
line(ax, [(44, 6), (44, 48)], 'fixe', dash=True)
text(ax, 22, 46, 'compter', 'autre', 'l', weight='bold')
text(ax, 66, 46, 'mesurer', 'sujet', 'l', weight='bold')
for i in range(6):
    for j in range(2):
        box(ax, 4 + i * 6.5, 25 + j * 7, 5, 5, 'autre', r=0.3)
text(ax, 22, 17, '12 chaises séparées', 'autre', 's')
box(ax, 50, 26, 36, 6, 'sujet', r=0.3)
for i in range(1, 6):
    line(ax, [(50 + i * 6, 26), (50 + i * 6, 32)], 'varie', lw=1.0)
text(ax, 68, 36, 'salle : 6 m', 'sujet', 's')
text(ax, 68, 17, '6 avec le mètre', 'varie', 's')
text(ax, 68, 10, '600 avec le cm', 'varie', 's')
save(fig, '11-014')
