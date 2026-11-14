import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 62, r'$R\,x$', 'sujet', 'xl', weight='bold')
text(ax, 22, 52, r'$R$ : les entiers $a$', 'fixe', 's')
text(ax, 66, 52, r'$x = (2\,;\,1)$', 'sujet', 's')
arrow(ax, (38, 59), (27, 55), 'fixe', lw=0.8); arrow(ax, (50, 59), (62, 55), 'fixe', lw=0.8)
text(ax, 44, 42, 'l’ensemble de tous les $a\\,x$', 'varie', 's')
for i, a in enumerate([-1, 0, 1, 2]):
    x0 = 3 + i * 21.5
    text(ax, x0 + 9.5, 33.5, f'a = {a}'.replace('-', '−'), 'varie', 's')
    box(ax, x0, 12, 19, 18, 'sujet', label=f'({2 * a} ; {a})'.replace('-', '−'), size='s')
text(ax, 44, 5, '…', 'sujet', 'l')
save(fig, '57-160')
