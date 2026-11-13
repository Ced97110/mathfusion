import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
for i in range(15):
    for j in range(9):
        disc(ax, 5.2 + 2.4*i, 59.2 + 2.4*j, 0.85, 'sujet', lw=0.5)
        disc(ax, 45.2 + 2.4*i, 59.2 + 2.4*j, 0.85, 'fixe', lw=0.5)
disc(ax, 83.5, 59.2, 0.85, 'limite', lw=0.5)
text(ax, 22, 83, '135 : 15 paquets de 9', 'sujet', 's')
text(ax, 62, 83, '136 : 15 paquets de 9', 'fixe', 's')
text(ax, 22, 54, 'reste 0', 'resultat', 'm')
text(ax, 64, 54, 'reste 1', 'limite', 'm')
line(ax, [(4, 45), (84, 45)], 'fixe', dash=True)
for cx in [12, 18, 24, 30]:
    box(ax, cx - 1.7, 15.8, 3.4, 10.4, 'autre', fill=False, r=0.5, lw=0.6)
    for y in [18, 21, 24]:
        disc(ax, cx, y, 1.0, 'autre', lw=0.5)
text(ax, 22, 32, '12 par 3 : 4 paquets', 'autre', 's')
box(ax, 50.3, 15.8, 9.4, 10.4, 'fixe', fill=False, r=0.5, lw=0.6)
for x in [52, 55, 58]:
    for y in [18, 21, 24]:
        disc(ax, x, y, 1.0, 'fixe', lw=0.5)
for y in [18, 21, 24]:
    disc(ax, 66, y, 1.0, 'limite', lw=0.5)
text(ax, 62, 32, '12 par 9 : 1 paquet + 3', 'limite', 's')
text(ax, 44, 8, 'divisible par 9 = reste 0', 'resultat', 'm')
save(fig, '01-147')
