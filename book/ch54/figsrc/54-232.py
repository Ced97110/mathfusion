import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(106)
text(ax, 44, 101, r'$f=x^3+x^2+2$, degré 3', 'sujet', 'l')
text(ax, 22, 90, 'modulo 3 : 3 valeurs', 'sujet', 's')
text(ax, 66, 90, r'dans $\mathbb{Z}$ : 4 valeurs', 'autre', 's')
left = [r'$f(0)=2$', r'$f(1)=1$', r'$f(2)=2$']
right = [r'$f(1)=4$', r'$f(-1)=2$', r'$f(2)=14$', r'$f(-2)=-2$']
for i, s in enumerate(left):
    box(ax, 4, 72 - i * 12, 36, 10, 'sujet', label=s, size='m')
for i, s in enumerate(right):
    box(ax, 46, 72 - i * 12, 38, 10, 'autre', label=s, size='m')
box(ax, 8, 6, 72, 12, 'resultat', label=r'irréductible sur $\mathbb{Q}$', size='m')
arrow(ax, (44, 24), (44, 19), 'resultat')
text(ax, 44, 27, 'aucune valeur nulle', 'resultat', 's')
save(fig, '54-232')
