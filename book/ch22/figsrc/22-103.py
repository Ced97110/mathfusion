import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
box(ax, 4, 72, 40, 10, 'sujet', label=r'$4\sqrt{32}+5\sqrt{2}$')
arrow(ax, (24, 72), (24, 56), 'varie'); text(ax, 28, 64, r'$\sqrt{32}=4\sqrt{2}$', 'varie', 's', ha='left')
box(ax, 4, 46, 40, 10, 'sujet', label=r'$16\sqrt{2}+5\sqrt{2}$')
arrow(ax, (24, 46), (24, 30), 'varie'); text(ax, 28, 38, r'$16+5=21$', 'varie', 's', ha='left')
box(ax, 4, 20, 40, 10, 'resultat', label=r'$21\sqrt{2}$')
text(ax, 24, 12, r'$\approx29{,}70$ avant et après', 'resultat', 's')
save(fig, '22-103')
