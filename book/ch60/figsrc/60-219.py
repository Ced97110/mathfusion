import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
w = 14; x0 = 9; y = 24
labs = ['1', 'A', '?', '?', '?']
for i in range(5):
    box(ax, x0 + i * w, y, w - 1, 12, 'sujet' if i < 2 else 'fixe', label=labs[i], size='l')
brace(ax, x0, x0 + 5 * w - 1, y + 12, 'encre', label=r'commutent avec $A$ : 5', down=False)
brace(ax, x0, x0 + 2 * w - 1, y, 'sujet', label=r'polynômes en $A$ : 2')
brace(ax, x0 + 2 * w, x0 + 5 * w - 1, y, 'fixe', label="d’autres matrices : 3")
save(fig, '60-219')
