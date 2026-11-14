import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 12, 42, 'p = 2', 'sujet', 'm')
text(ax, 12, 14, 'p = 3', 'sujet', 'm')
for i in range(3):
    box(ax, 26 + 12 * i, 38, 11, 8, 'sujet', label='2', size='l')
for i in range(2):
    box(ax, 26 + 12 * i, 10, 11, 8, 'sujet', label='3', size='l')
brace(ax, 26, 61, 47, 'varie', label='e = 3 facteurs', down=False)
brace(ax, 26, 49, 19, 'varie', label='e = 2 facteurs', down=False)
text(ax, 72, 42, '= 8', 'resultat', 'l')
text(ax, 60, 14, '= 9', 'resultat', 'l')
save(fig, '60-079')
