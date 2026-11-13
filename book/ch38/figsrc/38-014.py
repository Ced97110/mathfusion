import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
gy = 20
A, B, H, S = (8, gy), (28, gy), (68, gy), (68, 50)
line(ax, [(2, gy), (86, gy)], 'fixe')
line(ax, [A, S], 'fixe', lw=0.9, dash=True)
line(ax, [B, S], 'fixe', lw=0.9, dash=True)
line(ax, [S, H], 'fixe', lw=0.9, dash=True)
line(ax, [A, B], 'sujet', lw=2.6)
for x in (A[0], B[0]):
    disc(ax, x, gy, 1.3, 'sujet')
brace(ax, A[0], B[0], gy - 2, 'sujet', label='base : 1 000 m')
text(ax, 20, 44, 'visées : calculées', 'fixe', 's')
text(ax, 77, 34, 'ℎ : cherchée', 'fixe', 's')
save(fig, '38-014')
