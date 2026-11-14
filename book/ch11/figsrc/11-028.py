import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, '1 gallon = 4 quarts', 'sujet', 'm', weight='bold')
c = 6
for g in range(3):
    gx = 6 + g * (4 * c + 3)
    for i in range(4): box(ax, gx + i * c, 24, c, 8, 'varie', lw=0.6, r=0.3)
    box(ax, gx - 0.3, 22.5, 4 * c + 0.6, 11, 'sujet', fill=False, lw=1.0, r=0.3)
    text(ax, gx + 2 * c, 38, '1 gallon', 'sujet', 's')
brace(ax, 6, 6 + 3 * 24 + 6, 20, 'resultat', label='12 quarts', size='m')
text(ax, 44, 5, r'$3 \times 4 = 12$', 'varie', 'l')
save(fig, '11-028')
