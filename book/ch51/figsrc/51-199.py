import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
names = ['A1', 'A2', 'A3', 'A4', 'M1', 'M2', 'D1', 'D2']
used = {'A3', 'A4', 'D2'}
for i, n in enumerate(names):
    x = 2.5 + i*10.4
    box(ax, x, 38, 9, 9, 'sujet' if n in used else 'fixe', label=n, size='s', weight='bold' if n in used else 'normal')
text(ax, 44, 53, 'les huit règles', 'encre', 's')
text(ax, 44, 31, 'bleu : utilisées par la preuve', 'sujet', 's')
box(ax, 4, 6, 38, 12, 'limite', fill=False, dash=True, label=r'$ab=ba$', size='m')
box(ax, 46, 6, 38, 12, 'limite', fill=False, dash=True, label='division', size='m')
text(ax, 44, 23, 'jamais utilisées', 'limite', 's')
save(fig, '51-199')
