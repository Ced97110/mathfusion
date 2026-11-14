import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(92)
text(ax, 44, 86, r'dans $\mathbb{F}_2$ : $(u+v)^2 = u^2 + v^2$', 'resultat', 'm')
text(ax, 44, 78, r'$(1+1)^2 = 0^2 = 0$', 'resultat', 'm')
text(ax, 44, 71, r'$1^2 + 1^2 = 1 + 1 = 0$', 'resultat', 'm')
box(ax, 8, 51, 72, 10, 'varie', label=r'$g(\alpha^2) = 1 + \alpha^2 + \alpha^6 = 0$', size='s')
text(ax, 44, 45, r'car $\alpha^6 = 1 + \alpha^2$ : $\alpha^2$ est racine', 'varie', 's')
line(ax, [(2, 38), (86, 38)], 'fixe')
text(ax, 44, 32, 'avec les nombres ordinaires', 'limite', 's')
text(ax, 44, 24, r'$(1+1)^2 = 4$', 'limite', 'm')
text(ax, 44, 17, r'$1^2 + 1^2 = 2$', 'limite', 'm')
text(ax, 44, 8, r'$4 \neq 2$ : la racine en plus disparaît', 'limite', 's')
save(fig, '68-204')
