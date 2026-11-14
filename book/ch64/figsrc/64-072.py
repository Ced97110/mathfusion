import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 19, 86, 'suite normale', 'sujet', 's')
text(ax, 69, 86, 'suite de composition', 'resultat', 's')
ys = [72 - 15 * i for i in range(5)]
Lv = ['24', '12', '4', '2', '1']
for i, y in enumerate(ys):
    dashed = (i == 3)
    box(ax, 4, y, 30, 8, 'varie' if dashed else 'sujet', fill=not dashed, dash=dashed, label=Lv[i])
    box(ax, 54, y, 30, 8, 'resultat', label=Lv[i])
    if i < 4:
        arrow(ax, (19, y), (19, ys[i + 1] + 8), 'fixe', lw=0.8)
        arrow(ax, (62, y), (62, ys[i + 1] + 8), 'fixe', lw=0.8)
        # un groupe intercalé est impossible : case rouge pointillée barrée
        cy = y - 3.5
        box(ax, 70, cy - 2, 10, 4, 'limite', fill=False, dash=True, lw=0.7, r=0.5)
        line(ax, [(71, cy - 1.2), (79, cy + 1.2)], 'limite', lw=1.1)
        line(ax, [(71, cy + 1.2), (79, cy - 1.2)], 'limite', lw=1.1)
text(ax, 19, 3, 'on peut insérer 2', 'varie', 's')
text(ax, 69, 3, 'aucun terme à insérer', 'resultat', 's')
save(fig, '64-072')
