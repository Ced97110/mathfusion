import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, 'f : x ↦ 3x dans ℤ/12', 'varie', 'm')
text(ax, 17, 55, 'M', 'sujet', 'm')
text(ax, 71, 55, 'M', 'sujet', 'm')
L = {'1': 44, '5': 30, '4': 16}
for k, y in L.items():
    box(ax, 10, y, 14, 8, 'sujet', label=k)
R = {'3': 38, '0': 16}
for k, y in R.items():
    box(ax, 64, y, 14, 8, 'resultat', label=k)
arrow(ax, (24, 48), (64, 43), 'varie')
arrow(ax, (24, 34), (64, 41), 'varie')
arrow(ax, (24, 20), (64, 20), 'varie')
text(ax, 17, 6, '1 + 4 = 5', 'sujet', 's')
text(ax, 71, 6, '3 + 0 = 3', 'resultat', 's')
save(fig, '60-086')
