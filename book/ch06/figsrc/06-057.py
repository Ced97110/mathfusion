import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
q, x0 = 20, 14
box(ax, x0, 38, 3 * q, 10, 'sujet', label=r'barre $\frac{3}{4}$')
for k in range(3):
    box(ax, x0 + k * q, 26, q, 10, 'varie', label=r'$\frac{1}{4}$')
brace(ax, x0, x0 + 3 * q, 26, 'varie', label='combien de briques ?')
text(ax, x0 + 1.5 * q, 7, '3 briques', 'resultat', 'l', weight='bold')
save(fig, '06-057')
