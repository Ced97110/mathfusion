import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = [(r'$X_2Y_3$', '6 × 4 = 24', 'sujet'), (r'$X_3Y_2$', '5 × 0 = 0', 'autre'), ('différence', '24 − 0 = 24', 'varie'),
        ('valeur absolue', r'$|24|=24$   ou   $|-24|=24$', 'varie'), ('moitié', r'$\frac{1}{2}\times 24 = 12$', 'resultat')]
h, gap, top = 9.0, 4.5, 66.0
for i, (cap, lab, role) in enumerate(rows):
    y = top - h - i * (h + gap)
    text(ax, 31, y + h / 2, cap, role, 's', ha='right')
    box(ax, 34, y, 52, h, role, label=lab, size='s')
    if i < 4: arrow(ax, (60, y), (60, y - gap), 'fixe')
save(fig, '37-104')
