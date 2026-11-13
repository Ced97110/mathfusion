import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
w = 12
text(ax, 44, 44, r'$x^2$ + 5$x$ + 4 : le milieu', 'encre', 'm', weight='bold')
text(ax, 8, 35, r'attendu : 2 × $x$ × 2 = 4$x$', 'sujet', 's', ha='left')
for i in range(4): box(ax, 8 + i * w, 24, w, 8, 'sujet', label=r'$x$', r=0.4)
text(ax, 8, 17, r'présent : 5$x$', 'limite', 's', ha='left')
for i in range(5): box(ax, 8 + i * w, 6, w, 8, 'sujet' if i < 4 else 'limite', label=r'$x$', r=0.4)
text(ax, 8 + 4.5 * w + 6, 17, '1 de trop', 'limite', 's')
save(fig, '18-060')
