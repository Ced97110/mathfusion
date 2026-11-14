import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 94, '×3 : injectif', 'resultat', 'm', weight='bold')
for i, (a, b) in enumerate(zip((1, 2, 3, 4), (3, 6, 9, 12))):
    x = 14 + i * 20
    disc(ax, x, 80, 3.4, 'sujet', label=str(a), size='s'); disc(ax, x, 58, 3.4, 'resultat', label=str(b), size='s')
    arrow(ax, (x, 76.3), (x, 61.7), 'resultat')
text(ax, 44, 88, 'un seul entier par image', 'resultat', 's')
text(ax, 44, 46, 'le bouton : pas injectif', 'limite', 'm', weight='bold')
for i in range(6):
    disc(ax, 10 + i * 13.6, 32, 2.6, 'sujet')
for j in range(4):
    disc(ax, 20 + j * 16, 8, 2.6, 'limite')
for i in range(6):
    arrow(ax, (10 + i * 13.6, 29.2), (20 + min(i * 4 // 6, 3) * 16 if False else 20 + (i % 4) * 16, 10.8), 'limite', lw=0.7)
text(ax, 44, 40, 'une infinité d’entiers', 'sujet', 's'); text(ax, 78, 8, '4 images', 'limite', 's')
save(fig, '48-181')
