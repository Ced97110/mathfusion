import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
cw=26; xs=[5+i*cw for i in range(3)]
text(ax,44,70,'2 + 2 − 1 = 3','encre','l')
text(ax,5,63,'U : 2 dimensions','sujet','s',ha='left')
for i,n in enumerate(('profondeur','largeur')): box(ax,xs[i]+1,48,cw-2,10,'sujet',label=n,size='s')
text(ax,5,44,'W : 2 dimensions','autre','s',ha='left')
for i,n in enumerate(('largeur','hauteur')): box(ax,xs[i+1]+1,30,cw-2,10,'autre',label=n,size='s')
box(ax,xs[1],28,cw,32,'varie',fill=False,dash=True,lw=1.2)
text(ax,44,24.5,'compté deux fois','varie','s')
text(ax,5,19,'U + W : 3 dimensions','resultat','s',ha='left')
for i,n in enumerate(('profondeur','largeur','hauteur')): box(ax,xs[i]+1,4,cw-2,10,'resultat',label=n,size='s')
save(fig,'80-069')
