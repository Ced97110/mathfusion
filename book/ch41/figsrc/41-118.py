import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

j, k = (0, 1, 0), (0, 0, 1)
c = (j[1] * k[2] - j[2] * k[1], j[2] * k[0] - j[0] * k[2], j[0] * k[1] - j[1] * k[0])
assert c == (1, 0, 0)
fig, ax = canvas(50)
text(ax, 22, 45, r'$j=\langle 0,1,0\rangle$, $k=\langle 0,0,1\rangle$', 'encre', 's')
rows = [(r'$1\times1-0\times0=1$', 'resultat'), (r'$0\times0-0\times1=0$', 'fixe'), (r'$0\times0-1\times0=0$', 'fixe')]
for i, (lab, role) in enumerate(rows):
    box(ax, 3, 28 - i * 11, 38, 8, role, label=lab, size='s')
o = (66, 14); s = 12
I = lambda p: iso(p[0], p[1], p[2], o, s)
arrow(ax, I((0, 0, 0)), I(j), 'sujet', lw=1.2)
arrow(ax, I((0, 0, 0)), I(k), 'autre', lw=1.2)
arrow(ax, I((0, 0, 0)), I(c), 'resultat', lw=1.8)
text(ax, I(j)[0] - 1.5, I(j)[1] + 2.5, r'$j$', 'sujet', 'm')
text(ax, I(k)[0], I(k)[1] + 3, r'$k$', 'autre', 'm')
text(ax, I(c)[0] + 1.5, I(c)[1] + 2.5, r'$j\times k=i$', 'resultat', 's', ha='left')
save(fig, '41-118')
