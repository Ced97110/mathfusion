import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 82, 'premier 2 : 2 choix', 'sujet', 'm', weight='bold')
par = [(22, '2'), (66, '1 + 1')]
kids = ['3', '2 + 1', '1 + 1 + 1']
for px, pt in par:
    box(ax, px - 11, 62, 22, 9, 'sujet', label=pt)
    for k, kt in enumerate(kids):
        cx = px + (k - 1) * 14
        line(ax, [(px, 62), (cx, 49)], 'fixe')
        box(ax, cx - 6.5, 40, 13, 9, 'autre', label=kt, size='s')
text(ax, 44, 33, 'premier 3 : 3 choix pour chacun', 'autre', 'm', weight='bold')
text(ax, 44, 26, 'premier 5 : 1 seul choix', 'fixe', 's')
brace(ax, 3, 85, 20, 'resultat', label=r'$2\times3\times1=6$ combinaisons')
save(fig, '60-233')
