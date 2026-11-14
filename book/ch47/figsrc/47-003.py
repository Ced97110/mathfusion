import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 56, r'Un groupe de 8 éléments', 'sujet', 'l')
for i in range(8): disc(ax, 12 + i * 9.2, 46, 2.2, 'sujet')
text(ax, 44, 36, 'Un sous-groupe a combien d’éléments ?', 'encre', 'm')
for i in range(8):
    x = 6 + i * 10
    arrow(ax, (x + 4, 32), (x + 4, 25), 'fixe', lw=0.6)
    box(ax, x, 12, 8, 11, 'varie', label=str(i + 1), size='l')
text(ax, 44, 5, 'tailles possibles ?', 'varie', 'm')
save(fig, '47-003')
