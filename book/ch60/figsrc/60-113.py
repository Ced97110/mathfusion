import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, r'$\mathbb{Z}$ : abélien, une infinité d’éléments', 'limite', 's')
arrow(ax, (44, 58), (3, 58), 'limite', both=False)
arrow(ax, (44, 58), (85, 58), 'limite')
for k in range(-6, 7):
    disc(ax, 44 + 6 * k, 58, 1.3, 'limite')
text(ax, 44, 46, '≠', 'limite', 'xl', weight='bold')
text(ax, 44, 38, r'$\mathbb{Z}/4\oplus\mathbb{Z}/3$ : 12 éléments', 'sujet', 's')
for i in range(3):
    for j in range(4):
        disc(ax, 35 + j * 6, 26 - i * 6, 1.8, 'sujet')
text(ax, 44, 4, 'un produit de cycliques est fini', 'sujet', 's')
save(fig, '60-113')
