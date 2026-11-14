import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 92, 'Lagrange : classes de $H$', 'fixe', 's')
bx = [4 + i * 21 for i in range(4)]
for x in bx:
    box(ax, x, 72, 17, 12, 'fixe'); disc(ax, x + 5.5, 78, 2.3, 'fixe'); disc(ax, x + 11.5, 78, 2.3, 'fixe')
brace(ax, 4, 84, 70, 'fixe', label=r'$|G| = 8 = 4 \times 2$')
text(ax, 44, 57, 'même découpage', 'varie', 's')
text(ax, 44, 46, r'Action : classes de Stab $A$', 'sujet', 's')
for x, n in zip(bx, 'ABCD'):
    box(ax, x, 26, 17, 12, 'sujet'); disc(ax, x + 5.5, 32, 2.3, 'sujet'); disc(ax, x + 11.5, 32, 2.3, 'sujet')
    arrow(ax, (x + 8.5, 24), (x + 8.5, 14), 'varie'); disc(ax, x + 8.5, 9, 4, 'resultat', label=n, size='s')
save(fig, '49-164')
