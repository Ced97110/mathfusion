import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 9, 38, r'$D_1$', 'sujet'); text(ax, 9, 16, 'candidat', 'encre', 's')
box(ax, 20, 33, 18, 10, 'sujet', label=r'$x-1$'); box(ax, 40, 33, 18, 10, 'limite', fill=False, label=r'$x-1$', dash=True)
box(ax, 20, 11, 18, 10, 'sujet', label=r'$x-1$'); box(ax, 40, 11, 18, 10, 'autre', label=r'$x+3$')
line(ax, [(49, 31), (49, 23)], 'limite', dash=True)
text(ax, 72, 27, 'trop petit', 'limite', 'm')
text(ax, 44, 4, r'$D_1$ ne le divise pas', 'limite', 's')
save(fig, '21-073')
