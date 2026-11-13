import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72); c=13; x0=24; y0=26
vals=[[-1,0,0],[0,1,0],[0,0,1]]
for i in range(3):
    for j in range(3):
        v=vals[i][j]; r='varie' if v==-1 else ('sujet' if v==1 else 'fixe')
        box(ax,x0+j*c,y0+(2-i)*c,c,c,r,label=str(v).replace('-','−'))
brace(ax,x0,x0+c,y0+3*c+1,'varie',label=r'$u$',down=False); brace(ax,x0+c,x0+3*c,y0+3*c+1,'sujet',label=r'$H$',down=False)
text(ax,44,y0-6,r'$-1\times1\times1=-1$','resultat','m')
text(ax,44,y0-14,'déterminant −1 : impropre','resultat','s')
save(fig,'72-077')
