import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 44
box(ax, 4, y, 14, 9, 'sujet', label=r'$\sqrt{8}$')
arrow(ax, (20, y + 4.5), (34, y + 4.5), 'varie'); text(ax, 27, y + 11, 'on simplifie', 'varie', 's')
box(ax, 36, y, 18, 9, 'sujet', label=r'$2\sqrt{2}$')
box(ax, 64, y, 14, 9, 'sujet', label=r'$\sqrt{2}$')
brace(ax, 36, 78, y - 1, 'resultat', 'même radicande : 2', down=True)
box(ax, 14, 8, 20, 9, 'sujet', label=r'$\sqrt{2}$')
box(ax, 54, 8, 20, 9, 'autre', label=r'$\sqrt{3}$')
text(ax, 44, 4, 'pas semblables', 'limite', 's')
save(fig, '22-101')
