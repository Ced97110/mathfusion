import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
steps = [
    ('départ : p premier, p = b c', 'sujet'),
    ('p ∣ b c', 'sujet'),
    ('p ∣ b', 'varie'),
    ('b = p u   (car b ∣ p aussi)', 'sujet'),
    ('p = p u c', 'sujet'),
    ('arrivée : u c = 1, c unité', 'resultat'),
]
h, g = 11, 6.5
top = 102
ys = [top - i * (h + g) - h for i in range(len(steps))]
for (lab, role), y in zip(steps, ys):
    box(ax, 4, y, 50, h, role, label=lab, size='s')
for i in range(len(steps) - 1):
    arrow(ax, (29, ys[i] - 0.4), (29, ys[i + 1] + h + 0.4), 'fixe')
text(ax, 58, ys[2] + h / 2 + 8, 'définition de', 'varie', 's', ha='left')
text(ax, 58, ys[2] + h / 2 + 3.5, '« premier »', 'varie', 's', ha='left')
text(ax, 58, ys[2] + h / 2 - 2, 'étape clé', 'varie', 'm', ha='left')
text(ax, 58, ys[4] + h / 2 + 8, 'on simplifie par p', 'fixe', 's', ha='left')
text(ax, 58, ys[0] + h / 2, 'ici : p = 7,', 'resultat', 's', ha='left')
text(ax, 58, ys[0] + h / 2 - 4.5, 'b = 7, c = 1', 'resultat', 's', ha='left')
save(fig, '56-046')
