import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 8, 36, 16, 16, 'sujet', label=r'$U$', size='xl')
text(ax, 30, 44, '(', 'encre', 'xl')
box(ax, 36, 36, 16, 16, 'autre', label=r'$M$', size='xl')
text(ax, 58, 44, ')', 'encre', 'xl')
text(ax, 16, 30, 'les inversibles', 'sujet', 's')
text(ax, 16, 25, 'de', 'sujet', 's')
text(ax, 44, 30, 'le monoïde', 'autre', 's')
text(ax, 44, 25, 'de départ', 'autre', 's')
text(ax, 72, 44, r'$U(M)$', 'sujet', 'm') if False else None
arrow(ax, (44, 20), (44, 14), 'varie')
text(ax, 44, 8, r'autre monoïde $N$ : $U(N)$', 'varie', 'm')
save(fig, '44-110')
