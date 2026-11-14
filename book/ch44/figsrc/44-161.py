import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, R = 24, 40, 17
pos = {}
for i in range(5):
    a = math.pi / 2 - 2 * math.pi * i / 5
    pos[i] = (cx + R * math.cos(a), cy + R * math.sin(a))
    role = 'resultat' if i == 0 else ('varie' if i in (2, 3) else 'sujet')
    disc(ax, *pos[i], 4.2, role, label=str(i))
text(ax, cx, 70, r'$\mathbb{Z}_5$ : 5 heures', 'sujet', 'm')
items = [('Somme : encore une heure', 'sujet', 62), ('Neutre : 0', 'resultat', 49),
         ('Opposés : 2 et 3', 'varie', 36), ('Ordre des termes sans effet', 'fixe', 23)]
for s, r, y in items:
    box(ax, 46, y, 40, 9, r, label=s, size='s')
box(ax, 46, 8, 40, 9, 'sujet', label='5 éléments : ordre 5', size='s', weight='bold')
save(fig, '44-161')
