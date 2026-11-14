import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
gy = 14
line(ax, [(6, gy), (82, gy)], 'fixe', lw=1.4)
text(ax, 82, gy - 3.5, 'plan (sol)', 'fixe', 's', ha='right')
A, Hh, G = (10, gy), (66, gy), (66, gy + 28)
line(ax, [Hh, G], 'fixe', lw=1.0, dash=True)
s = 3.5
line(ax, [(66 - s, gy), (66 - s, gy + s), (66, gy + s)], 'encre', lw=0.7)
line(ax, [A, G], 'autre', lw=1.8)
line(ax, [A, Hh], 'sujet', lw=3.0)
for p, c in ((A, 'sujet'), (Hh, 'sujet'), (G, 'autre')): disc(ax, *p, 1.4, c)
text(ax, A[0], gy - 4, r'$A$', 'sujet', 'm')
text(ax, Hh[0], gy - 4, r'$H$', 'sujet', 'm')
text(ax, G[0] + 4, G[1], r'$G$', 'autre', 'm')
text(ax, 30, 36, r'$AG$', 'autre', 'm')
text(ax, 38, 8, r'$AH$ = projeté de $AG$', 'sujet', 'm')
text(ax, 38, 21, r'$AH$ = 5 m', 'sujet', 's')

text(ax, 66, G[1] + 6, 'perpendiculaire au plan', 'fixe', 's', ha='right')
save(fig, '27-058')
