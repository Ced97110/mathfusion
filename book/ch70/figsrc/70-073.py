import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 54, 'liste de nombres', 'fixe', 's')
for i, v in enumerate(['2', '3', '4']):
    box(ax, 22 + i * 16, 38, 12, 10, 'fixe', label=v, size='l')
arrow(ax, (32, 37.5), (22, 26), 'autre')
arrow(ax, (56, 37.5), (66, 26), 'sujet')
text(ax, 16, 32, r'$\sum$', 'autre', 'xl')
text(ax, 72, 32, r'$\prod$', 'sujet', 'xl')
box(ax, 2, 14, 40, 11, 'autre', label=r'$2+3+4=9$')
box(ax, 46, 14, 40, 11, 'sujet', label=r'$2\times3\times4=24$')
text(ax, 22, 8, 'additionne', 'autre', 's')
text(ax, 66, 8, 'multiplie', 'sujet', 's')
save(fig, '70-073')
