import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# (5, 4) = 5 e1 + 4 e2 : 5 sacs de riz, 4 sacs de lentilles ; avec 6 sacs de riz : autre vente
text(ax, 44, 58, r'$(5,\ 4) = 5\,e_1 + 4\,e_2$', 'encre', 'xl', weight='bold')
s, step, x0 = 5.4, 6.4, 26
text(ax, 2, 44.5, r'5 sacs $e_1$', 'sujet', 's', ha='left')
text(ax, 2, 31.5, r'4 sacs $e_2$', 'autre', 's', ha='left')
for i in range(5):
    box(ax, x0 + i * step, 41, s, s, 'sujet', r=0.5)
for i in range(4):
    box(ax, x0 + i * step, 28, s, s, 'autre', r=0.5)
text(ax, 2, 12.5, r'6 sacs $e_1$', 'limite', 's', ha='left')
for i in range(6):
    box(ax, x0 + i * step, 9, s, s, 'limite' if i == 5 else 'fixe', r=0.5, dash=(i == 5))
text(ax, 86, 12.2, r'$(6,\ 4) \neq (5,\ 4)$', 'limite', 's', ha='right')
save(fig, '58-008')
