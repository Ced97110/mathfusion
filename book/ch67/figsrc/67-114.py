import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, r'polynômes unitaires de degré 2 sur $\mathbb{F}_2$', 'encre', 's')
P = [(r'$x^2$', r'$x\cdot x$', 'fixe'), (r'$x^2+1$', r'$(x+1)(x+1)$', 'fixe'),
     (r'$x^2+x$', r'$x(x+1)$', 'fixe'), (r'$x^2+x+1$', 'irréductible', 'resultat')]
for i, (p, f, r) in enumerate(P):
    x = 3 + i * 21.5
    box(ax, x, 48, 20, 11, r, label=p, size='s')
    text(ax, x + 10, 42, f, r, 's')
brace(ax, 3, 85, 64, 'sujet', label=r'$q^n=4$ polynômes', down=False)
box(ax, 14, 8, 60, 12, 'resultat', label=r'$N(2,2)=1$ : un seul', size='m')
arrow(ax, (75, 38), (66, 21), 'resultat')
save(fig, '67-114')
