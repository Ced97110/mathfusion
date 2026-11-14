import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$f(x,y)=y^2+1$', 'encre', 'm')
text(ax, 13, 57, 'couple', 'fixe', 'm')
text(ax, 41, 57, 'réels ?', 'fixe', 'm')
text(ax, 71, 57, r'$f=0$ ?', 'fixe', 'm')
ok, no = ('✓', 'resultat'), ('✗', 'limite')
rows = [(r'$(5,\ 0)$', 'fixe', ok, no), (r'$(5,\ i)$', 'fixe', no, ok), (r'$(a,\ b)$', 'sujet', ok, ok)]
for r, (lab, role, m1, m2) in enumerate(rows):
    y = 41 - r * 14
    box(ax, 2, y, 22, 11, role, label=lab, size='s')
    box(ax, 28, y, 26, 11, m1[1], label=m1[0], size='l')
    box(ax, 58, y, 26, 11, m2[1], label=m2[0], size='l')
text(ax, 44, 8, 'point réel : les deux ✓', 'sujet', 'm')
save(fig, '70-082')
