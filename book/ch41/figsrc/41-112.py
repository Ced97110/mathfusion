import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

u, v = (2, 0, 0), (1, 2, 0)
c = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
assert c == (0, 0, 4)
fig, ax = canvas(48)
text(ax, 44, 43, r'$\langle 2,0,0\rangle\times\langle 1,2,0\rangle=\langle 0,0,4\rangle$', 'encre', 'm')
o = (14, 6); s = 5
I = lambda p: iso(p[0], p[1], p[2], o, s)
poly(ax, [I((0, 0, 0)), I(u), I((3, 2, 0)), I(v)], 'sujet')
arrow(ax, I((0, 0, 0)), I(u), 'sujet', lw=1.0)
arrow(ax, I((0, 0, 0)), I(v), 'autre', lw=1.0)
arrow(ax, I((0, 0, 0)), I(c), 'resultat', lw=1.6)
text(ax, I(u)[0] + 2, I(u)[1] - 2, r'$u$', 'sujet', 's')
text(ax, I(v)[0] - 2, I(v)[1] + 1, r'$v$', 'autre', 's')
text(ax, I(c)[0] + 2, I(c)[1] + 1, r'$k$ ×4', 'resultat', 's', ha='left')
rows = [(r'$0\times0-0\times2=0$', 'fixe'), (r'$0\times1-2\times0=0$', 'fixe'), (r'$2\times2-0\times1=4$', 'resultat')]
for i, (lab, role) in enumerate(rows):
    box(ax, 40, 26 - i * 10, 46, 8, role, label=lab, size='s')
save(fig, '41-112')
