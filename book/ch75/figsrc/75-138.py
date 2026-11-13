import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 4, 46, r'$|O_3(\mathbb{F}_3)|$', 'autre', 's', ha='left')
box(ax, 4, 28, 26, 11, 'autre', label='24'); box(ax, 31, 28, 26, 11, 'autre', label='24')
text(ax, 71, 33.5, '= 48', 'autre', 'l', weight='bold')
text(ax, 4, 20, r'$|Sp_2(\mathbb{F}_3)|=3\times8$', 'sujet', 's', ha='left')
box(ax, 4, 4, 26, 11, 'sujet', label='24')
text(ax, 44, 9.5, r'$\times\,2$ donne $O_3$', 'varie', 's', ha='left')
save(fig, '75-138')
