import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
u=4.4; y0=20; X=[3,33,63]
sq=lambda x,y,w,h:[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
poly(ax,sq(X[0],y0,5*u,5*u),'sujet'); text(ax,X[0]+2.5*u,y0+2.5*u,r'$(a+b)^2$','sujet','s')
text(ax,X[0]+2.5*u,y0-4,r'$a+b$','sujet','s')
for (i,j,w,h) in [(0,0,3,3),(3,0,2,3),(0,3,3,2),(3,3,2,2)]: poly(ax,sq(X[1]+i*u,y0+j*u,w*u,h*u),'fixe')
line(ax,[(X[1]+3*u,y0-1),(X[1]+3*u,y0+5*u+1)],'varie',dash=True); line(ax,[(X[1]-1,y0+3*u),(X[1]+5*u+1,y0+3*u)],'varie',dash=True)
text(ax,X[1]+1.5*u,y0-4,r'$a$','sujet','s'); text(ax,X[1]+4*u,y0-4,r'$b$','autre','s')
for (i,j,w,h,r,l) in [(0,0,3,3,'sujet',r'$a^2$'),(3,0,2,3,'varie',r'$ab$'),(0,3,3,2,'varie',r'$ab$'),(3,3,2,2,'autre',r'$b^2$')]:
    poly(ax,sq(X[2]+i*u,y0+j*u,w*u,h*u),r); text(ax,X[2]+(i+w/2)*u,y0+(j+h/2)*u,l,r,'s')
text(ax,X[2]+2.5*u,y0-4,r'$a^2+2ab+b^2$','resultat','s')
for a,b in [(27,30.5),(57,60.5)]: arrow(ax,(a,y0+2.5*u),(b,y0+2.5*u),'fixe')
for k,c in enumerate(['départ','on coupe','arrivée']): text(ax,X[k]+2.5*u,47,c,'encre','s')
save(fig,'15-099')
