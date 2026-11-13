import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 22, 61, 'écriture longue', 'fixe', 's'); text(ax, 70, 61, 'écriture courte', 'fixe', 's')
for k, n in enumerate(['12', '5', '8']):
    y = 42 - k * 15
    box(ax, 6, y, 32, 11, 'sujet', label=r'ℤ/%sℤ' % n)
    text(ax, 46, y + 5.5, '=', 'resultat', 'xl')
    box(ax, 54, y, 32, 11, 'sujet', label=r'ℤ$_{%s}$' % n)
text(ax, 44, 68, r'ℤ/$n$ℤ  =  ℤ$_n$ : même ensemble', 'resultat', 'm')
text(ax, 44, 6, 'plus court : 2 signes au lieu de 4', 'varie', 's')
save(fig, '44-141')
