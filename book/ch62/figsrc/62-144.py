import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
# p = 2 : x^2 - t irréductible sur F, mais (x - b)^2 dans un corps plus grand
box(ax, 14, 76, 60, 14, 'sujet', label=r'$f=x^2-t$' + '\nirréductible sur $F$', size='s')
arrow(ax, (44, 76), (44, 65), 'varie', lw=1.2)
text(ax, 49, 70.5, r'corps plus grand : $b^2=t$', 'varie', 's', ha='left')
box(ax, 8, 51, 72, 13, 'fixe', label=r'$x^2-b^2=(x-b)^2$')
text(ax, 44, 45, r'car $1+1=0$ : $-b=b$', 'fixe', 's')
# une seule racine, comptée deux fois
line(ax, [(8, 30), (80, 30)], 'fixe')
disc(ax, 44, 30, 4, 'autre', label=r'$b$', size='m')
text(ax, 55, 30, r'$\times\,2$', 'varie', 'l')
text(ax, 44, 21, 'une seule racine, deux fois', 'autre', 's')
box(ax, 8, 4, 72, 11, 'resultat', label=r"$f\,'=2x=0$, donc $(f,f\,')=f\neq1$", size='s')
save(fig, '62-144')
