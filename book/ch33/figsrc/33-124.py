import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 4; A = (4, 14); B = (A[0]+4*s, A[1]); C = (B[0], A[1]+3*s)
poly(ax, [A, B, C], 'fixe')
line(ax, [A, B], 'sujet', lw=2.0); line(ax, [B, C], 'sujet', lw=2.0); line(ax, [A, C], 'autre', lw=2.0)
text(ax, (A[0]+B[0])/2, A[1]-3, '4', 'sujet', 's'); text(ax, B[0]+2.5, (B[1]+C[1])/2, '3', 'sujet', 's')
text(ax, 8, A[1]+9, '5', 'autre', 's')
u = 8; x0 = 40
for i, (n, r) in enumerate(((3, 'sujet'), (4, 'sujet'), (5, 'autre'))):
    y = 42 - i*10
    box(ax, x0, y, n*u, 7, r, label=str(n))
text(ax, 60, 11, r'$\frac{3}{5}<1$  et  $\frac{4}{5}<1$', 'resultat', 'm')
text(ax, 60, 4, 'l’hypoténuse est la plus longue', 'autre', 's')
save(fig, '33-124')
