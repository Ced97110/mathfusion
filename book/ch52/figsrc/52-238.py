import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
w_=6.6; g=0.8; x0=3.7; y=18
for i in range(10): box(ax,x0+i*(w_+g),y,w_,10,'sujet',lw=0.6,r=0.5,label='19' if i==0 else None,size='s')
x=x0+10*(w_+g)
box(ax,x,y,w_,10,'fixe',fill=False,dash=True,lw=0.6,r=0.5)
box(ax,x,y,w_*10/19,10,'varie',lw=0.6,r=0.3)
brace(ax,x0,x0+11*w_+10*g,y+11.5,'fixe',label='200 chiffres',down=False)
brace(ax,x0+0.3,x-g-0.3,y-1,'limite',label='10 cases × 19 = 190 : trop peu',down=True)
brace(ax,x+0.3,x+w_-0.3,y-1,'varie',label='+ 10',down=True)
text(ax,44,5,'il faut au moins 11 cases','resultat','m')
save(fig,'52-238')
