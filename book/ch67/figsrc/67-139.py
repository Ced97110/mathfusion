import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [(66, r'$u=2+i$', r'$T(u)=1$'), (50, r'$v=1$', r'$T(v)=2$'), (28, r'$u+v=3+i$', r'$T(u+v)=0$')]
for n, (y, l, r) in enumerate(rows):
    box(ax, 10, y, 30, 9, 'fixe', label=l, size='s')
    box(ax, 50, y, 30, 9, 'sujet', label=r, size='s')
    arrow(ax, (40.5, y + 4.5), (49.5, y + 4.5), 'sujet')
text(ax, 45, 73.5, r'$T$', 'sujet', 's')
line(ax, [(10, 70.5), (7, 70.5), (7, 32.5)], 'varie', lw=1.0)
line(ax, [(10, 54.5), (7, 54.5)], 'varie', lw=1.0)
arrow(ax, (7, 32.5), (9.8, 32.5), 'varie')
text(ax, 3.2, 52, 'additionner', 'varie', 's', rot=90)
line(ax, [(80, 70.5), (83, 70.5), (83, 32.5)], 'varie', lw=1.0)
line(ax, [(80, 54.5), (83, 54.5)], 'varie', lw=1.0)
arrow(ax, (83, 32.5), (80.2, 32.5), 'varie')
text(ax, 85.8, 52, r'$1+2=0$', 'varie', 's', rot=90)
text(ax, 44, 17, r'$T(u+v)=T(u)+T(v)$', 'resultat', 'l')
text(ax, 44, 6, r'$T(au)=a\,T(u)$ pour $a\in F$', 'sujet', 'l')
save(fig, '67-139')
