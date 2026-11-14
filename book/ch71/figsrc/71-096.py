import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
x0,y0,c=24,12,20
text(ax,10,y0+c,r'$S=$','encre','l')
for i,t in enumerate((r'$e_1$',r'$e_2$')):
    text(ax,x0+c/2+i*c,y0+2*c+5,t,'sujet' if i==0 else 'autre','s')
    text(ax,x0-5,y0+c*1.5-i*c,t,'sujet' if i==0 else 'autre','s')
vals=((0,0,'0','fixe'),(0,1,'1','varie'),(1,0,r'$-1$','varie'),(1,1,'0','fixe'))
for r_,c_,s,role in vals:
    box(ax,x0+c_*c+1,y0+(1-r_)*c+1,c-2,c-2,role,label=s,size='l')
arrow(ax,(x0+c*2+3,y0+c*1.5),(x0+c*2+3,y0+c*0.5),'varie',curve=-0.0,both=True) if False else None
arrow(ax,(x0+c+4,y0+c+4),(x0+c-4,y0+c-4),'varie',lw=1.2,both=True)
text(ax,x0+2*c+3,y0+c,'1 et −1 : opposés','varie','s',ha='left')
text(ax,x0+2*c+4,y0+c*1.5+4,'diagonale','fixe','s',ha='left') if False else None
text(ax,44,5,'diagonale nulle','fixe','s')
save(fig,'71-096')
