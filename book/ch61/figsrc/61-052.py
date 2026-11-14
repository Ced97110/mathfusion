import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 4, 22, 16, 16, 'sujet', label=r'$\pi$', size='xl')
text(ax, 12, 16, 'base : ℚ', 'fixe', 's')
for i, lab in enumerate([r'$f_1(\pi)\neq 0$', r'$f_2(\pi)\neq 0$', r'$f_3(\pi)\neq 0$']):
    y = 42 - i * 14
    box(ax, 40, y - 5, 28, 10, 'limite', label=lab, size='s')
    arrow(ax, (20.5, 30), (39.5, y), 'varie')
text(ax, 54, 52, 'polynômes non nuls', 'fixe', 's')
text(ax, 77, 21, '…', 'limite', 'l')
text(ax, 44, 6, 'aucun polynôme ne s\'annule', 'limite', 'm')
save(fig, '61-052')
