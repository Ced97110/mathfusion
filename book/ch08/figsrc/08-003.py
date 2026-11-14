import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$2+\frac{35}{100}$ plus $1+\frac{8}{10}$', 'sujet', 'm')
rows = [('convertir', r'$\frac{8}{10}=\frac{80}{100}$', 'varie'),
        ('additionner', r'$35+80=115$', 'varie'),
        ('comparer à 100', r'$115>100$', 'varie'),
        ('reporter 1 mètre', r'$4+\frac{15}{100}$', 'resultat')]
ys = [50, 34, 18, 2]
for (lab, expr, role), y in zip(rows, ys):
    text(ax, 3, y + 6, lab, 'encre', 'm', ha='left')
    box(ax, 44, y, 40, 12, role, label=expr, size='m')
for y in ys[:-1]:
    arrow(ax, (64, y), (64, y - 4), 'fixe')
save(fig, '08-003')
