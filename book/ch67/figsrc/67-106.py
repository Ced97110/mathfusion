import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'cherche $d\times k=12$ sans reste', 'encre', 's')
items = [(1, 12, 'sujet'), (2, 6, 'varie'), (3, 4, 'varie'), (4, 3, 'resultat'), (6, 2, 'resultat'), (12, 1, 'sujet')]
for i, (d, k, r) in enumerate(items):
    row, c = divmod(i, 3)
    box(ax, 3 + c * 28.5, 30 - row * 15, 27, 11, r, label=rf'${d}\times{k}=12$', size='m')
brace(ax, 3, 85.5, 11, 'fixe', label='6 diviseurs : 6 sous-corps', down=True)
save(fig, '67-106')
