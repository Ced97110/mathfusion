import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 4, 40, 36, 15, 'sujet', label='500 motifs', size='l')
box(ax, 48, 40, 36, 15, 'sujet', label='5 millions', size='l')
text(ax, 44, 59, 'motifs différents', 'fixe', 's')
arrow(ax, (22, 38), (30, 25), 'varie', lw=1.0); arrow(ax, (66, 38), (58, 25), 'varie', lw=1.0)
w = 4.0
for i in range(17): box(ax, 4 + i * 4.94, 15, w + 0.3, 9, 'resultat', r=0.3)
brace(ax, 4, 4 + 16 * 4.94 + w + 0.3, 13, 'resultat', '17 listes seulement', down=True, size='m')
save(fig, '74-004')
