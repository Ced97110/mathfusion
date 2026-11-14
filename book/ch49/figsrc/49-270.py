import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'cycles $c$, puis valeur $2^{c}$', 'encre', 'm')
cyc = [8, 6, 6, 6, 4, 4]; val = [256, 64, 64, 64, 16, 16]
roles = ['fixe', 'varie', 'varie', 'varie', 'autre', 'autre']
dx = 13.0; x0 = 44 - dx * 2.5
for i in range(6):
    x = x0 + dx * i
    box(ax, x - 5, 52, 10, 10, roles[i], label=str(cyc[i]), size='m')
    arrow(ax, (x, 51), (x, 41), roles[i], lw=1.0)
    box(ax, x - 5.5, 28, 11, 10, roles[i], label=str(val[i]), size='s')
brace(ax, x0 - 5.5, x0 + dx * 5 + 5.5, 26, 'resultat', 'somme 480 ; 480 ÷ 6 = 80')
text(ax, 44, 10, r'$k=80$', 'resultat', 'xl', weight='bold')
save(fig, '49-270')
