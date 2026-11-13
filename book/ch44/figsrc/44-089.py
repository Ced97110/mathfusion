import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, 'triangle', 'sujet', 'm')
for i in range(6): box(ax, 9 + i * 11, 42, 9, 9, 'sujet')
brace(ax, 9, 74, 41, 'sujet', r'$|M|=6$', down=True)
text(ax, 44, 24, 'carreau', 'autre', 'm')
for i in range(8): box(ax, 3 + i * 10.5, 7, 8.5, 9, 'autre')
brace(ax, 3, 85, 6, 'autre', r'$|M|=8$', down=True)
save(fig, '44-089')
