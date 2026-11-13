import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
steps = [('sujet', r'$x^3-3x-1$', 'départ'), ('varie', 'racines possibles : 1 ou −1', 'étape clé'),
         ('limite', 'x = 1 : 1 − 3 − 1 = −3 ≠ 0', None), ('limite', 'x = −1 : −1 + 3 − 1 = 1 ≠ 0', None),
         ('resultat', 'irréductible : degré 3', 'arrivée')]
for i, (r, t, tag) in enumerate(steps):
    y = 67 - 16 * i
    box(ax, 22, y, 64, 11, r, label=t, weight='bold' if i == 1 else 'normal')
    if tag: text(ax, 2, y + 5.5, tag, 'fixe', 's', ha='left')
    if i < 4: arrow(ax, (54, y), (54, y - 5), 'fixe')
save(fig, '61-194')
