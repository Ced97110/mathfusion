import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'polynôme minimal de degré $n=4$', 'encre', 's')
labs = [r'$x^4$', r'$c_1x^3$', r'$c_2x^2$', r'$c_3x$', r'$c_4=1$']
for k, lab in enumerate(labs):
    last = (k == 4)
    box(ax, 3 + 17.2 * k, 52, 14, 10, 'autre' if last else 'fixe', label=lab, size='s')
arrow(ax, (78.8, 51.5), (78.8, 44), 'autre')
box(ax, 26, 34, 58, 10, 'autre', label=r'$N(u)=(-1)^4\times1=1$')
text(ax, 44, 26, r'signe $(-1)^n$ : parité de $n$', 'encre', 's')
for k, (lab, role) in enumerate([(r'$n=2$ : $+1$', 'fixe'), (r'$n=3$ : $-1$', 'varie'), (r'$n=4$ : $+1$', 'autre')]):
    box(ax, 6 + 28 * k, 10, 24, 10, role, label=lab, size='s')
save(fig, '67-144')
