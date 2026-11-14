import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, '1 pied = 12 po', 'sujet', 'l', weight='bold')
x0, c = 4.4, 2.2
for p in range(3):
    box(ax, x0 + p * 12 * c, 24, 12 * c, 10, 'sujet', lw=0.9, r=0.3)
    for i in range(1, 12): line(ax, [(x0 + (p * 12 + i) * c, 24.5), (x0 + (p * 12 + i) * c, 28)], 'fixe', lw=0.5)
    text(ax, x0 + (p * 12 + 6) * c, 38, '1 pied', 'sujet', 's')
brace(ax, x0, x0 + 36 * c, 22, 'resultat', label='36 po', size='m')
text(ax, 44, 6, r'$3 \times 12 = 36$', 'varie', 'l')
save(fig, '11-024')
