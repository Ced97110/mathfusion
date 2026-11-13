import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for i in range(4): disc(ax, 14 + i * 20, 20, 5, 'sujet', label=str(i + 1))
for a in (0, 2):
    arrow(ax, (14 + a * 20 + 2, 25.2), (14 + a * 20 + 18, 25.2), 'varie', curve=-0.6, both=True)
text(ax, 24, 40, '(1 2)', 'varie', 'm'); text(ax, 64, 40, '(3 4)', 'varie', 'm')
text(ax, 44, 7, 'deux échanges, aucune carte commune', 'encre', 's')
save(fig, '46-238')
