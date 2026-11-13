import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 55, r'$(2^2)^3$', 'sujet', 'xl')
for g in range(3):
    x = 6 + g*27
    box(ax, x, 26, 22, 14, 'sujet', fill=False, dash=True)
    box(ax, x + 3, 29.5, 7, 7, 'sujet', label='2'); box(ax, x + 12, 29.5, 7, 7, 'sujet', label='2')
    text(ax, x + 11, 45, r'$2^2$', 'sujet')
brace(ax, 6, 82, 24, 'fixe', label='3 groupes de 2 facteurs')
box(ax, 20, 3, 48, 9, 'resultat', label=r'6 facteurs $= 3 \times 2$')
save(fig, '14-043')
