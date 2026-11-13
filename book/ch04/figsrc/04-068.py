import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'2 + 3 $\times$ 4', 'sujet', 'l')
for x, lab, role in [(16, 'vous', 'encre'), (44, 'camarade', 'encre'), (72, 'sans la règle', 'limite')]:
    arrow(ax, (44, 62), (x, 50), 'varie')
    text(ax, x, 47, lab, role, 's')
for x, lab, role in [(4, '14', 'resultat'), (32, '14', 'resultat'), (60, '20', 'limite')]:
    box(ax, x, 30, 24, 12, role, fill=False, label=lab, size='l')
text(ax, 16, 24, '2 + 12', 'resultat', 'm')
text(ax, 44, 24, '2 + 12', 'resultat', 'm')
text(ax, 72, 24, r'5 $\times$ 4', 'limite', 'm')
brace(ax, 4, 56, 19, 'resultat', label='une seule valeur : 14', down=True, size='s')
text(ax, 72, 14, 'gauche → droite', 'limite', 's')
save(fig, '04-068')
