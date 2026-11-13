import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'conjuguer $H$ par chaque $g$ de $G$', 'varie', 's')
cw = 12; gap = 1; x0 = 44 - (6 * cw + 5 * gap) / 2
names = ['$e$', '$r$', '$r^2$', '$s_A$', '$s_B$', '$s_C$']
xs = []
for i, n in enumerate(names):
    box(ax, x0 + i * (cw + gap), 56, cw, 10, 'fixe', label=n, size='m')
    xs.append(x0 + i * (cw + gap) + cw / 2)
bw = 40
box(ax, 44 - bw / 2, 22, bw, 12, 'sujet', label=r'$H$ = 3 rotations', size='m')
for i, x in enumerate(xs):
    tx = 44 - 14 + i * 5.6
    arrow(ax, (x, 55), (tx, 35), 'varie', lw=0.9)
text(ax, 44, 14, 'un seul conjugué : $H$', 'sujet', 's')
text(ax, 44, 6, r'$[G:N(H)] = 6\ /\ 6 = 1$', 'resultat', 'm', weight='bold')
save(fig, '50-079')
