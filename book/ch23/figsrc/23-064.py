import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 2, 56, 34, 12, 'fixe', label='discriminant'); arrow(ax, (37, 62), (56, 62), 'varie'); text(ax, 46, 67, '1re lettre', 'varie', 's')
box(ax, 58, 54, 14, 16, 'sujet', label=r'$D$', size='xl', weight='bold')
box(ax, 8, 30, 18, 12, 'sujet', label=r'$D$', size='l'); text(ax, 31, 36, '=', 'encre', 'l'); box(ax, 36, 30, 44, 12, 'sujet', label=r'$b^2-4ac$', size='l')
box(ax, 8, 6, 30, 12, 'sujet', label=r'si $D>0$'); text(ax, 43, 12, 'au lieu de', 'varie', 's'); box(ax, 56, 6, 30, 12, 'fixe', label=r'si $b^2-4ac>0$', size='s')
save(fig, '23-064')
