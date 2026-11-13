import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
rows = [('un quotient', r'$0^5 / 0^2 = 0 \div 0$'), ('un exposant nul', r'$0^0$ : preuve par $0 \div 0$'), ('un exposant négatif', r'$0^{-2} = 1 \div 0^2 = 1 \div 0$')]
text(ax, 4, 67, 'avec la base 0, on trouve :', 'fixe', 's', ha='left')
for i, (h, s) in enumerate(rows):
    y = 48 - i * 15
    text(ax, 4, y + 12.5, h, 'fixe', 's', ha='left')
    box(ax, 4, y, 54, 9, 'limite', label=s, size='s')
    arrow(ax, (58, y + 4.5), (64, 34), 'limite')
box(ax, 64, 26, 21, 17, 'limite', label=r'$\div\ 0$', size='l')
text(ax, 74.5, 21, 'impossible', 'limite', 's')
box(ax, 4, 2, 80, 8, 'resultat', label=r'$a \neq 0$ : aucune division par 0', size='m')
save(fig, '14-094')
