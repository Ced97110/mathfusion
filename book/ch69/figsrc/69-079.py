import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 28, 58, 'trois prémisses à vérifier', 'sujet', 's')
text(ax, 74, 58, 'une conclusion', 'resultat', 'm')
labs = ['(1) ℝ est un corps réel clos', r'(2) $f$ de degré 3', r'(3) $f(-2)=-1$, $f(2)=3$ non nuls']
ys = [42, 28, 14]
for y, lab in zip(ys, labs):
    box(ax, 2, y, 52, 11, 'sujet', label=lab, size='s')
    line(ax, [(54.5, y + 5.5), (58, y + 5.5)], 'fixe')
line(ax, [(58, 19.5), (58, 47.5)], 'fixe')
arrow(ax, (58, 33.5), (61.5, 33.5), 'fixe')
box(ax, 62, 22, 24, 24, 'resultat', label=r'$V(-2)-V(2)$' + '\n' + r'$=3-0=3$')
save(fig, '69-079')
