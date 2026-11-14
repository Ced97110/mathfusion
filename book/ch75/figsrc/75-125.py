import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 20, 46, 'formule', 'sujet', 's'); text(ax, 72, 46, 'déjà compté', 'autre', 's')
for y, f, n, s in [(30, r'$2\times 3$', '6', r'$SL_{2}(\mathbb{F}_{2})$'), (10, r'$3\times 8$', '24', r'$SL_{2}(\mathbb{F}_{3})$')]:
    box(ax, 3, y - 6, 26, 12, 'sujet', label=f, size='m'); box(ax, 62, y - 6, 24, 12, 'autre', label=s, size='s')
    box(ax, 37, y - 6, 17, 12, 'resultat', label=n, size='l')
    arrow(ax, (29.5, y), (36.5, y), 'varie'); arrow(ax, (61.5, y), (54.5, y), 'varie')
save(fig, '75-125')
