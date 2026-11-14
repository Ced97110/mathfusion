import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 30, 87, r'$A=x^2+2$ et $B=2x$', 'encre', 'm')
steps = [(r'$(A-B)(A+B)$', 'sujet'),
         (r'$A^2-B^2$', 'varie'),
         (r'$(x^2+2)^2-(2x)^2$', 'fixe'),
         (r'$x^4+4x^2+4-4x^2$', 'fixe'),
         (r'$x^4+4$', 'resultat')]
y = 70
tops = []
for lab, role in steps:
    box(ax, 2, y, 56, 9, role, label=lab, size='m')
    tops.append(y)
    y -= 14
for i in range(len(steps) - 1):
    arrow(ax, (30, tops[i] - 0.3), (30, tops[i + 1] + 9.3), 'fixe')
text(ax, 73, tops[1] + 4.5, 'étape clé :\nidentité', 'varie', 's', weight='bold')
text(ax, 73, tops[3] + 4.5, 'les $4x^2$\nse détruisent', 'fixe', 's')
text(ax, 73, tops[0] + 4.5, r'$x=1$ : $1\times5$', 'encre', 's')
text(ax, 73, tops[2] + 4.5, r'$x=1$ : $9-4$', 'encre', 's')
save(fig, '54-213')
