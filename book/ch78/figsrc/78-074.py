import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
u = 8
for y, v, lab, role in [(36, 5, r'$|x|=\sqrt{5}$', 'sujet'), (24, 13, r'$|y|=\sqrt{13}$', 'autre'), (12, 65, r'$|xy|=\sqrt{65}$', 'resultat')]:
    box(ax, 4, y, math.sqrt(v) * u, 8, role, label=lab, size='s')
line(ax, [(4, 10), (4, 46)], 'fixe', dash=True)
text(ax, 44, 4, r'$\sqrt{5}\times\sqrt{13}=\sqrt{65}$', 'resultat', 'm')
save(fig, '78-074')
