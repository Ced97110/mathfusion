import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
u=2.5; x0=6; y=18
for k in range(6):
    xa=x0+5*k*u; xb=xa+5*u
    role='resultat' if k==4 else ('sujet' if k%2==0 else 'fixe')
    poly(ax,[(xa,y),(xb,y),(xb,y+12),(xa,y+12)],role)
f=numberline(ax,x0,x0+75,y,0,30,step=5,labels=True,arrow_right=False,size='s')
disc(ax,f(23),y+4,1.2,'encre'); text(ax,f(23),y+8.5,'23','resultat','s')
for v in (20,23): line(ax,[(f(v),y+12),(f(v),y+17)],'resultat',dash=True)
arrow(ax,(f(20),y+17),(f(23),y+17),'resultat')
text(ax,(f(20)+f(23))/2,y+21,'r = 3','resultat','s')
brace(ax,f(20),f(25),y-6.5,'fixe',label='case de longueur 5')
text(ax,x0,y+30,'ni trou, ni chevauchement','encre','s',ha='left')
save(fig,'05-040')
