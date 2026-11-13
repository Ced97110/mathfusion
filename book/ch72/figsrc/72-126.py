import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 2, 67, r'$V$ : $n=3$ dimensions', 'sujet', 's', ha='left')
for i in range(3): box(ax, 8 + i * 15.5, 50, 14, 12, 'sujet')
text(ax, 2, 40, r'$\nu=2$ plans $H_i$ : 4 dimensions', 'autre', 's', ha='left')
for i in range(4): box(ax, 8 + i * 15.5, 22, 14, 12, 'limite' if i == 3 else 'autre')
brace(ax, 8, 37, 20, 'autre', r'$H_1$'); brace(ax, 39, 68.5, 20, 'autre', r'$H_2$')
text(ax, 79, 28, r'$4>3$', 'limite', 'm', weight='bold')
save(fig, '72-126')
