import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
n = 15
bw1 = 72 / n
for i in range(n):
    box(ax, 8 + i * bw1, 38, bw1, 8, 'sujet', r=0.3, lw=0.6)
brace(ax, 8, 80, 48, 'fixe', label='30 cm : paquets de 2 cm', down=False)
arrow(ax, (44, 36), (44, 27), 'varie')
text(ax, 50, 31.5, r'$\div 2$ les deux longueurs', 'varie', 's', ha='left')
bw2 = bw1 / 2
for i in range(n):
    box(ax, 8 + i * bw2, 14, bw2, 8, 'resultat', r=0.2, lw=0.5)
brace(ax, 8, 8 + n * bw2, 13, 'fixe', label='15 cm : paquets de 1 cm')
text(ax, 62, 18, '15 paquets', 'resultat', 's', weight='bold')
text(ax, 44, 57, 'toujours 15 paquets', 'encre', 'l')
save(fig, '09-036')
