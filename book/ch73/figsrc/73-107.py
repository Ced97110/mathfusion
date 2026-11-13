import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arcarr(ax,c,r,a0,a1,role,lw=1.0):
    n=24; pts=[(c[0]+r*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+r*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw); arrow(ax,pts[-2],pts[-1],role,lw)

fig,ax=canvas(64); s=7; o=(46,10)
pl=lambda x,y:(o[0]+s*x,o[1]+s*y)
line(ax,[pl(-3.4,0),pl(4,0)],'fixe',lw=0.5); line(ax,[pl(0,-0.3),pl(0,4)],'fixe',lw=0.5)
P,Q,S=pl(3,2),pl(-2,3),pl(0,3)
arcarr(ax,o,s*math.sqrt(13),math.degrees(math.atan2(2,3))+2,math.degrees(math.atan2(3,-2))-3,'sujet',lw=1.3)
arrow(ax,(Q[0]+1.5,Q[1]),(S[0]-1.5,S[1]),'varie',lw=1.3)
disc(ax,*P,1.2,'encre'); disc(ax,*Q,1.2,'fixe'); disc(ax,*S,1.2,'resultat')
text(ax,P[0]+3,P[1],'(3 ; 2)','encre','s',ha='left')
text(ax,Q[0]-1,Q[1]+4,'(−2 ; 3)','fixe','s'); text(ax,S[0]+2,S[1]-4.5,'(0 ; 3)','resultat','s',ha='left')
text(ax,60,46,'A : quart de tour','sujet','s',ha='left'); text(ax,Q[0]+3,Q[1]-4.5,r'$x=(2\,;\,0)$','varie','s')
box(ax,8,50,12,9,'sujet',label='A',size='l'); box(ax,24,50,12,9,'varie',label=r'$x$',size='l')
text(ax,22,62,'couple (A, x)','encre','s')
save(fig,'73-107')
