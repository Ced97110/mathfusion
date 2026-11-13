import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 1, 4, 38, 40, 'sujet', fill=False)
text(ax, 20, 49, 'les huit règles', 'sujet', 'm', weight='bold')
names = ['A1', 'A2', 'A3', 'A4', 'M1', 'M2', 'D1', 'D2']
for i, n in enumerate(names):
    box(ax, 4 + (i % 2) * 17.5, 33 - (i // 2) * 9.5, 15.5, 8, 'sujet', label=n, size='s')
text(ax, 66, 49, 'pas dans la liste', 'fixe', 'm', weight='bold')
for i, s in enumerate([r'$ab=ba$', 'on peut diviser', r'$1\neq0$']):
    box(ax, 44, 33 - i * 14, 42, 11, 'fixe', fill=False, dash=True, label=s, size='m')
save(fig, '51-043')
