import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 14, 76, 60, 10, 'sujet', label=r'$[x+y,\,x+y] = 0$')
arrow(ax, (44, 76), (44, 67), 'varie')
text(ax, 44, 63, 'on développe en 4 crochets', 'varie', 's')
labs = [(r'$[x,x]$', 'fixe'), (r'$[x,y]$', 'varie'), (r'$[y,x]$', 'varie'), (r'$[y,y]$', 'fixe')]
for k, (l, r) in enumerate(labs):
    box(ax, 3 + k * 21.5, 44, 19, 11, r, label=l, size='s')
    if r == 'fixe':
        arrow(ax, (12.5 + k * 21.5, 44), (12.5 + k * 21.5, 36), 'fixe', lw=0.8)
        box(ax, 3 + k * 21.5, 26, 19, 9, 'fixe', label=r'$=0$', size='s')
text(ax, 44, 20, r'$[x,y]+[y,x]=0$', 'resultat', 'm')
arrow(ax, (44, 17), (44, 10), 'resultat')
text(ax, 44, 5, r'$[x,y]=-[y,x]$', 'resultat', 'l')
save(fig, '78-045')
