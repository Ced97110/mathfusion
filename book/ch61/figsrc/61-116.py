import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'extension finie : 3 briques', 'sujet', 'm', weight='bold')
for i in range(3): box(ax, 18 + i * 20, 47, 16, 11, 'sujet', label='brique', size='s')
for i, n in enumerate(['1', r'$u$', r'$u^2$', r'$u^3$']): box(ax, 8 + i * 20, 27, 16, 11, 'varie', label=n, size='m')
brace(ax, 8, 84, 25.5, 'varie', label='4 nombres pour 3 briques : liés', size='s')
arrow(ax, (44, 15), (44, 10), 'resultat', lw=1.2)
box(ax, 4, 1, 80, 9, 'resultat', label=r'un polynôme non nul s’annule en $u$', size='s')
save(fig, '61-116')
