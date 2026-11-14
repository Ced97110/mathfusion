import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# départ à 3 cases, arrivée à 2 cases : 3 colonnes, 2 lignes
cw, ch, g = 11, 9, 1.5
mx, my = 30, 14
for j in range(2):
    for i in range(3):
        box(ax, mx + i * (cw + g), my + (1 - j) * (ch + g), cw, ch, 'fixe', label=r'$a_{%d%d}$' % (j + 1, i + 1), size='s', r=0.5)
for i in range(3):
    text(ax, mx + i * (cw + g) + cw / 2, 40, r'$e_%d$' % (i + 1), 'sujet', 'm', weight='bold')
for j in range(2):
    text(ax, mx - 6, my + (1 - j) * (ch + g) + ch / 2, r'$f_%d$' % (j + 1), 'autre', 'm', weight='bold')
brace(ax, mx, mx + 3 * cw + 2 * g, 45, 'sujet', label='3 colonnes : 3 sacs de départ', down=False)
line(ax, [(mx - 12, my + ch * 2 + g), (mx - 12, my)], 'autre')
text(ax, 11, my + ch + g / 2, '2 lignes :\n2 cases\nd’arrivée', 'autre', 's')
save(fig, '58-204')
