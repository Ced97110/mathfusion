import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 78, 'différence de carrés', 'sujet', 's')
for i, (a, b, ra, rb) in enumerate([(r'$a^2$', r'$x^2$', 'sujet', 'sujet'), ('$-$', '$+$', 'fixe', 'limite'), (r'$b^2$', '1', 'sujet', 'sujet')]):
    xc = 24 + i * 20
    box(ax, xc - 8, 62, 16, 10, ra, label=a)
    box(ax, xc - 8, 48, 16, 10, rb, label=b)
text(ax, 84, 53, '', 'encre')
text(ax, 44, 38, 'il y a un plus, pas un moins', 'limite', 's')
text(ax, 44, 30, 'trinôme', 'sujet', 's')
box(ax, 4, 14, 36, 11, 'sujet', label=r'$x^2+bx+c$')
box(ax, 48, 14, 36, 11, 'limite', label=r'$x^2+0x+1$')
text(ax, 44, 6, '', 'encre')
save(fig, '18-095')
