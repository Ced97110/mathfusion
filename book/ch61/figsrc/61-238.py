import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
line(ax, [(44, 8), (44, 66)], 'fixe', dash=True)
text(ax, 22, 60, r'$\mathbb{Z}/4\mathbb{Z}$', 'limite', 'm'); text(ax, 66, 60, 'corps à 4 éléments', 'resultat', 'm')
for i, (lab, role) in enumerate([('0', 'fixe'), ('1', 'fixe'), ('2', 'limite'), ('3', 'fixe')]):
    disc(ax, 22 + (i - 1.5) * 10, 40, 4.4, role, label=lab)
for i, (lab, role) in enumerate([('0', 'fixe'), ('1', 'resultat'), (r'$u$', 'resultat'), (r'$1+u$', 'resultat')]):
    disc(ax, 66 + (i - 1.5) * 10, 40, 4.4, role, label=lab, size='s')
text(ax, 22, 26, r'$2\times 2=0$, $2\neq 0$', 'limite', 's'); text(ax, 22, 18, '2 sans inverse', 'limite', 's')
text(ax, 66, 26, r'$u\times(1+u)=1$', 'resultat', 's'); text(ax, 66, 18, 'tout non nul : inverse', 'resultat', 's')
save(fig, '61-238')
