import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('3 × 5', '15', 1), ('15 × 17', '255', 3), ('255 × 257', '65 535', 5), ('65 535 × 65 537', '4 294 967 295', 10)]
d_of = [2, 3, 5, 10]
for i, ((m, v, _), d) in enumerate(zip(rows, d_of)):
    y = 50 - 14 * i
    box(ax, 2, y, 34, 10, 'varie', label=m, size='m')
    w = 14 + 2.8 * d
    box(ax, 44, y, w, 10, 'resultat' if i == 3 else 'sujet', label=v, size='m')
    arrow(ax, (36.5, y + 5), (43.5, y + 5), 'varie')
text(ax, 44, 67, 'plus de 4 milliards de côtés', 'resultat', 'm')
save(fig, '66-106')
