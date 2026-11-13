import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(75)
# carré de côté 5 : 25 cellules de 7 mm
for i in range(5):
    for j in range(5):
        box(ax, 8 + 7*i, 24 + 7*j, 7, 7, 'sujet', r=0.2)
text(ax, 5, 41.5, '5', 'sujet', 's')
brace(ax, 8, 43, 22, 'sujet', label='5', size='s')
text(ax, 25.5, 70, r'$5^{2}$ = 5 × 5 = 25 carreaux', 'resultat', 'm')
text(ax, 67, 66, 'exposant → nom', 'encre', 's')
box(ax, 48, 50, 38, 10, 'sujet', label=r'$5^{2}$ : « au carré »', lw=1.4)
box(ax, 48, 36, 38, 10, 'autre', label=r'$5^{3}$ : « au cube »')
box(ax, 48, 22, 38, 10, 'fixe', label=r'$5^{4}$ : « puissance 4 »')
arrow(ax, (48, 55), (43.8, 55), 'sujet')
text(ax, 67, 15, 'carré = 2 facteurs, une aire', 'sujet', 's')
text(ax, 25.5, 8, '« 5 puissance 2 » : même 25', 'fixe', 's')
save(fig, '04-023')
