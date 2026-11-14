import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
w, g, x0 = 18.0, 3.6, 2.6
cx = [x0 + w / 2 + i * (w + g) for i in range(4)]
vals = [r'$-1$', r'$0$', r'$1$', r'$9/4$']
for i in range(4):
    box(ax, cx[i] - w / 2, 34, w, 14, 'fixe' if i == 1 else 'sujet', label=rf'$f_{i}(1)$' + '\n' + vals[i], dash=(i == 1))
for i, s in ((0, '−'), (2, '+'), (3, '+')):
    text(ax, cx[i], 28, s, 'sujet', 'l', weight='bold')
text(ax, cx[1], 28, 'effacé', 'fixe', 's')
line(ax, [(cx[0], 24), (cx[0], 21), (cx[2], 21), (cx[2], 24)], 'varie')
text(ax, cx[1], 17, '1 changement', 'varie', 's')
line(ax, [(cx[2] + 2, 24), (cx[2] + 2, 21), (cx[3], 21), (cx[3], 24)], 'fixe')
text(ax, (cx[2] + 2 + cx[3]) / 2, 17, 'aucun', 'fixe', 's')
box(ax, 28, 2, 32, 9, 'resultat', label=r'$V(1)=1$', size='l')
save(fig, '69-091')
