import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [(r'$r_1^{9}=r_1^{8}\,r_1$', 'couper un facteur', 'sujet'),
        (r'$=(r_1^{4})^{2}\,r_1$', 'puissance de puissance', 'sujet'),
        (r'$=r_0^{2}\,r_1$', r'$r_1^{4}=r_0$ (4 quarts)', 'sujet'),
        (r'$=r_1$', r'$r_0$ disparaît (neutre)', 'sujet')]
ys = [64, 50, 36, 22]
for (eq, rule, role), y in zip(rows, ys):
    box(ax, 3, y, 44, 10, role, label=eq, size='l')
    text(ax, 52, y + 5, rule, 'varie', 's', ha='left')
for y in ys[:-1]:
    arrow(ax, (25, y), (25, y - 4), 'fixe')
arrow(ax, (25, 22), (25, 18), 'fixe')
box(ax, 3, 6, 82, 11, 'resultat', label=r'exposant $1<4$ : on s\'arrête'.replace("\\'", "’"), size='m')
save(fig, '45-225')
