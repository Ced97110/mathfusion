import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62); c=11
text(ax,44,57,'n cases = dimension de V','fixe','s')
for r,n in enumerate((2,3,4)):
    y=40-r*17
    text(ax,4,y+c/2,f'n = {n}','encre','m',ha='left')
    for i in range(n):
        box(ax,28+i*(c+1.5),y,c,c,'sujet' if i<n-1 else 'varie')
    text(ax,28+n*(c+1.5)+1,y+c/2,f'H : {n-1}','sujet','s',ha='left')
box(ax,28,2,6,5,'sujet'); text(ax,36,4.5,'H','sujet','s',ha='left')
box(ax,46,2,6,5,'varie'); text(ax,54,4.5,r'$u$','varie','s',ha='left')
save(fig,'72-070')
