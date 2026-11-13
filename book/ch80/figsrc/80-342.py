import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
gx, gy, c = 8, 18, 5
for i in range(6):
    for j in range(5):
        box(ax, gx + c * i, gy + c * j, c, c, 'sujet', r=0.3, lw=0.6)
arrow(ax, (gx, gy + 28), (gx + 30, gy + 28), 'sujet', both=True)
text(ax, gx + 15, gy + 32, r'$d=6$', 'sujet', 'm')
arrow(ax, (gx + 34, gy), (gx + 34, gy + 25), 'resultat', both=True)
text(ax, gx + 40, gy + 12.5, '5', 'resultat', 'l')
text(ax, gx + 15, gy - 4.5, '30 cases', 'fixe', 's')
text(ax, 66, 48, r'$30\div6=5$', 'resultat', 'l')
box(ax, 50, 22, 36, 9, 'resultat', label='PGCD(6, 5) = 1')
box(ax, 50, 9, 36, 9, 'resultat', label='PPCM(6, 5) = 30')
text(ax, 68, 35, 'complément de 6 :', 'resultat', 's')
save(fig, '80-342')
