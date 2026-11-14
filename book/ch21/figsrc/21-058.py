import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
for x, a, b, r in [(16, r'$\frac{2}{3}$', r'$\frac{2}{3}$', 'sujet'), (44, '÷', '×', 'varie'), (72, r'$\frac{5}{7}$', r'$\frac{7}{5}$', 'autre')]:
    box(ax, x - 10, 56, 20, 16, r, label=a, size='l')
    box(ax, x - 10, 28, 20, 16, r, label=b, size='l')
    arrow(ax, (x - 6, 54), (x - 6, 46), 'fixe' if x == 16 else 'varie')
text(ax, 12, 50, 'pareil', 'fixe', 's', ha='left')
text(ax, 40, 50, 'devient ×', 'varie', 's', ha='left')
text(ax, 68, 50, 'retourné', 'varie', 's', ha='left')
arrow(ax, (44, 27), (44, 20), 'varie')
box(ax, 14, 4, 60, 15, 'resultat', label=r'$\frac{2}{3}\times\frac{7}{5}=\frac{14}{15}$', size='l')
save(fig, '21-058')
