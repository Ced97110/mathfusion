import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 40, 'diviseurs de 12', 'sujet', 'm')
for i, d in enumerate([1, 2, 3, 4, 6, 12]):
    box(ax, 3 + 14 * i, 20, 12, 15, 'varie' if d == 6 else 'sujet', label=f'{d}\n?', size='m')
brace(ax, 3, 85, 19, 'fixe', label='6 questions : oui ou non')
text(ax, 44, 5, r'sous-groupe de $d$ éléments ?', 'encre', 'm')
save(fig, '50-003')
