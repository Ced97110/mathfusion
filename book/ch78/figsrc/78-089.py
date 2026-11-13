import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
xs = [6, 24, 42, 60]
lab = [(r'$u=2$', 'sujet'), (r'$x=3$', 'autre'), (r'$y=4$', 'autre'), (r'$u=2$', 'sujet')]
for x, (l, r) in zip(xs, lab): box(ax, x, 28, 16, 10, r, label=l)
brace(ax, 6, 40, 40, 'sujet', r'$ux=6$', down=False)
brace(ax, 42, 76, 40, 'sujet', r'$yu=8$', down=False)
text(ax, 41, 52, r'$(ux)(yu)=6\cdot8=48$', 'resultat', 'm')
brace(ax, 24, 58, 26, 'varie', r'$xy=12$', down=True)
text(ax, 41, 14, r'$u(xy)u=2\cdot12\cdot2=48$', 'resultat', 'm')
save(fig, '78-089')
