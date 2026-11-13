import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'si $a\ E\ b$ alors $b\ E\ a$', 'sujet', 'm')
for y, name, a, b, ans in ((40, 'même chiffre des unités', '13', '23', ('oui', 'oui')),
                           (12, 'plus petit ou égal', '2', '3', ('oui', 'non'))):
    text(ax, 3, y + 12, name, 'fixe', 's', ha='left')
    disc(ax, 30, y, 5, 'sujet', label=a); disc(ax, 70, y, 5, 'autre', label=b)
    for dy, tag, (p, q) in ((2.2, ans[0], ((36, 64), 0)), (-2.2, ans[1], ((64, 36), 1))):
        role = 'resultat' if tag == 'oui' else 'limite'
        arrow(ax, (p[0], y+dy), (p[1], y+dy), role)
        text(ax, 50, y + dy + (3.2 if dy > 0 else -3.2), tag, role, 's')
save(fig, '43-025')
