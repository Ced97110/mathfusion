import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 74, 'Avant : « quel côté ? »', 'encre', 'm')
arrow(ax, (40, 74), (55, 74), 'varie')
text(ax, 66, 74, r'Après : $\sqrt{A}$', 'sujet', 'l')
text(ax, 44, 58, r'même écriture pour chaque $A$', 'sujet', 's')

def carre(x0, y0, n, cote):
    c = cote / n
    for i in range(n):
        for j in range(n):
            box(ax, x0 + i * c, y0 + j * c, c, c, 'fixe', fill=False, lw=0.4, r=0)
    box(ax, x0, y0, cote, cote, 'sujet', fill=False, lw=1.2, r=0)

carre(10, 18, 6, 21.6)
carre(50, 18, 7, 25.2)
text(ax, 20.8, 44, r'$A$ = 36', 'sujet', 'm')
text(ax, 62.6, 48, r'$A$ = 49', 'sujet', 'm')
brace(ax, 10, 31.6, 16, 'resultat', label=r'$\sqrt{36}$ = 6', down=True, size='m')
brace(ax, 50, 75.2, 16, 'resultat', label=r'$\sqrt{49}$ = 7', down=True, size='m')
save(fig, '04-067')
