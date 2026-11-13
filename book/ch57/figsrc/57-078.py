import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 17, 60, '$R$', 'varie', 'm')
text(ax, 70, 60, 'End M', 'fixe', 'm')
box(ax, 2, 12, 30, 44, 'varie', fill=False, dash=True)
box(ax, 54, 12, 32, 44, 'fixe', fill=False, dash=True)
for y, a, r in [(38, '3', 'tripler'), (20, '2', 'doubler')]:
    box(ax, 6, y, 22, 9, 'varie', label=a)
    box(ax, 58, y, 24, 9, 'fixe', label=r)
    arrow(ax, (29, y + 4.5), (57, y + 4.5), 'sujet', lw=1.3)
    text(ax, 43, y + 8, r'$\eta$', 'sujet', 'm')
text(ax, 43, 5, 'η : le nom de cette flèche', 'sujet', 's')
save(fig, '57-078')
