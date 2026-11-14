import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0 = 8; pitch = 13
for i in range(5):
    disc(ax, x0 + i*pitch + 6, 56, 5, 'fixe' if i == 0 else 'sujet', label=str(i), size='m')
text(ax, 44, 63, r'$p=5$ est premier', 'encre', 's')
brace(ax, x0 + pitch + 1, x0 + 4*pitch + 11, 48, 'sujet', label=r'4 cases $=5-1$')
box(ax, 8, 12, 72, 14, 'varie', lw=1.8)
text(ax, 44, 22, r'Euler avec $\varphi(5)=4$', 'varie', 'm')
text(ax, 44, 16, r'case 2 : $2^4=16$', 'varie', 's')
arrow(ax, (44, 36), (44, 27), 'encre')
box(ax, 26, 1, 36, 6, 'resultat', label=r'$16=3\times5+1$ : reste 1', size='s')
save(fig, '47-196')
