import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
c1, c2, cy = (22, 66), (66, 66), 66
text(ax, 22, 83, 'horloge à 12', 'sujet', 'm'); text(ax, 66, 83, 'horloge à 4', 'resultat', 'm')
for k in range(12):
    a = math.radians(90 - 30 * k); x, y = c1[0] + 13 * math.cos(a), cy + 13 * math.sin(a)
    ker = k % 4 == 0
    disc(ax, x, y, 2.0, 'sujet' if ker else 'fixe')
    if ker: text(ax, c1[0] + 7.5 * math.cos(a), cy + 7.5 * math.sin(a), str(k), 'sujet', 's')
for k in range(4):
    a = math.radians(90 - 90 * k); x, y = c2[0] + 8 * math.cos(a), cy + 8 * math.sin(a)
    disc(ax, x, y, 2.0, 'resultat')
    text(ax, c2[0] + 3.6 * math.cos(a), cy + 3.6 * math.sin(a), str(k), 'resultat', 's')
arrow(ax, (38, cy), (54, cy), 'varie')
text(ax, 46, cy + 4, 'reste ÷ 4', 'varie', 's')
text(ax, 4, 41, '1. homomorphisme : reste ÷ 4', 'varie', 'm', ha='left')
text(ax, 4, 31, '2. noyau : 0, 4, 8', 'sujet', 'm', ha='left')
text(ax, 4, 21, '3. image : horloge à 4', 'resultat', 'm', ha='left')
text(ax, 4, 11, '4. théorème fondamental', 'encre', 'm', ha='left')
save(fig, '48-203')
