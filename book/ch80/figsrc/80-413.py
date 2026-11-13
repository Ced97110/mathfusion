import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
text(ax, 44, 51, r"$x^4-x=x\,(x+1)\,(x^2+x+1)$", 'encre', 'm')
u = 18; x0 = 8
parts = [(1, 'sujet', r"$x$", 'degré 1'), (1, 'sujet', r"$x+1$", 'degré 1'), (2, 'varie', r"$x^2+x+1$", 'degré 2')]
x = x0
for d, role, lab, dg in parts:
    box(ax, x, 24, d * u, 12, role, label=lab, size='m')
    text(ax, x + d * u / 2, 19, dg, role, 's')
    x += d * u
brace(ax, x0, x, 37.5, 'fixe', label=r"degré de $x^4-x$ : 4", down=False)
text(ax, 44, 8, r"$1\times2+2\times1=4$", 'resultat', 'm')
save(fig, '80-413')
