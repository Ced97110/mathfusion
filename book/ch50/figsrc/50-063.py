import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 21, 62, 'écriture produit', 'fixe', 's'); text(ax, 67, 62, 'écriture additive', 'sujet', 's')
rows = [(42, r"un élément : $hk$", r"un élément : $h + k$"), (24, r"l'ensemble : $HK$", r"l'ensemble : $H + K$")]
for y, l, r in rows:
    box(ax, 3, y, 36, 11, 'fixe', label=l, size='s')
    box(ax, 49, y, 36, 11, 'sujet', label=r, size='s')
    arrow(ax, (39.8, y + 5.5), (48.2, y + 5.5), 'varie', both=True)
text(ax, 44, 12, r"horloge : $3 + 2 = 5$", 'sujet', 's')
text(ax, 44, 5, "même ensemble, autre écriture", 'varie', 's')
save(fig, '50-063')
