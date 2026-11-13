import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
xs=[8+12*i for i in range(7)]; y=30
for i,x in enumerate(xs):
    disc(ax,x,y,4.2,'fixe' if i==0 else 'sujet',fill=(i>0),label=str(i))
brace(ax,xs[1]-4.2,xs[6]+4.2,y+8,'sujet',label=r'$D^*$',down=False,size='l')
text(ax,xs[0],y-9,'0 : retiré','limite','s')
text(ax,44,10,r'$D^*$ : tout $D$ sauf 0','sujet','m')
save(fig,'51-227')
