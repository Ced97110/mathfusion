import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
for c in range(4):
    for r in range(c + 1):
        box(ax, 8 + 4*c, 60 + 4*r, 4, 4, 'sujet', r=0.2, lw=0.5)
brace(ax, 8, 24, 58, 'sujet', label='1 + 2 + 3 + 4 = 10')
text(ax, 60, 76, 'de n = 4 à n + 1 = 5', 'fixe', 's')
for r in range(5):
    box(ax, 24, 60 + 4*r, 4, 4, 'varie', r=0.2, lw=0.5)
text(ax, 26, 84, '+ 5', 'varie', 'm')
box(ax, 6, 40, 26, 8, 'sujet', label=r'$n(n + 1)/2$')
text(ax, 35, 44, '+', 'encre', 'm')
box(ax, 38, 40, 16, 8, 'varie', label=r'$n + 1$')
text(ax, 72, 44, 'n = 4 : 10 + 5', 'encre', 's')
arrow(ax, (46, 39.5), (14, 28.5), 'varie', curve=0.3)
text(ax, 64, 34, 'mise en facteur', 'varie', 's')
box(ax, 6, 20, 16, 8, 'varie', label=r'$n + 1$')
text(ax, 25, 24, r'$\times$', 'encre', 'm')
box(ax, 28, 20, 22, 8, 'sujet', label=r'$n/2 + 1$')
text(ax, 74, 24, '5 × 3', 'encre', 's')
arrow(ax, (17, 19.5), (17, 12.5), 'fixe')
box(ax, 6, 4, 40, 8, 'resultat', label=r'$(n + 1)(n + 2)/2$')
text(ax, 72, 8, '15 = 5 × 6/2', 'encre', 's')
save(fig, '01-127')
