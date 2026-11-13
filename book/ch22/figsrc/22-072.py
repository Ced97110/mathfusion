import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 12; x0 = 24
box(ax, x0, 44, s, s, role='sujet', fill=True, label='aire 3', size='s')
text(ax, x0+s+3, 50, r'côté $\sqrt{3}$', 'sujet', 'm', ha='left')
text(ax, 4, 31, r'$2\sqrt{3}$', 'varie', 'l', ha='left')
for i in range(2): box(ax, x0+i*s, 28, s, 6, role='sujet', fill=True, label=r'$\sqrt{3}$', size='s')
text(ax, 4, 13, r'$5\sqrt{3}$', 'varie', 'l', ha='left')
for i in range(5): box(ax, x0+i*s, 10, s, 6, role='sujet', fill=True, label=r'$\sqrt{3}$', size='s')
save(fig, '22-072')
