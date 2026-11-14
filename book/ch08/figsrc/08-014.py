import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
vals = [r'$\frac{1}{10}$', r'$\frac{1}{100}$', r'$\frac{1}{1000}$', r'$\frac{1}{10\,000}$']
roles = ['varie', 'resultat', 'sujet', 'autre']
for i in range(4):
    box(ax, 5 + 16.5 * i, 22, 13, 16, roles[i], label=vals[i], size='s')
box(ax, 5 + 16.5 * 4, 22, 13, 16, 'fixe', fill=False, dash=True, label='…', size='l')
arrow(ax, (5, 14), (87, 14), 'varie')
text(ax, 44, 7, '÷10 à chaque place, sans fin', 'varie', 's')
save(fig, '08-014')
