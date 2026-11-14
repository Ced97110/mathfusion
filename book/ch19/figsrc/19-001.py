import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 11, 46, 'cahiers', 'sujet', 's'); text(ax, 69, 46, 'euros', 'resultat', 's')
for y, a, b, c in [(30, 3, 6, 7), (8, 5, 10, 11)]:
    box(ax, 3, y, 16, 10, 'sujet', label=str(a), size='l')
    box(ax, 36, y, 16, 10, 'fixe', label=str(b), size='l')
    box(ax, 61, y, 16, 10, 'resultat', label=str(c), size='l')
    arrow(ax, (20, y + 5), (35, y + 5), 'varie'); text(ax, 27.5, y + 8.5, r'$\times$ 2', 'varie', 's')
    arrow(ax, (53, y + 5), (60, y + 5), 'varie'); text(ax, 56.5, y + 8.5, '+ 1', 'varie', 's')
save(fig, '19-001')
