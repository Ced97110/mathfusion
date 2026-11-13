import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
# left: plane with two points
o=(8,14); s=6
arrow(ax,o,(o[0]+22,o[1]),'fixe',lw=0.7); arrow(ax,o,(o[0],o[1]+24),'fixe',lw=0.7)
A=(o[0]+2*s,o[1]); B=(o[0],o[1]+s)
disc(ax,*A,1.1,'sujet'); disc(ax,*B,1.1,'autre')
text(ax,A[0]+1,A[1]-4,'(2, 0)','sujet','s'); text(ax,B[0]+9,B[1]+3,'(0, 1)','autre','s')
text(ax,20,44,'plan','fixe','m')
# right: line
o2=(48,14); k=5.2
arrow(ax,o2,(o2[0]+2*k*3.4,o2[1]+k*3.4),'resultat',lw=1.4)
T=(o2[0]+4*k,o2[1]+2*k)
disc(ax,*T,1.3,'resultat')
text(ax,T[0]+2,T[1]-5,'(4, 2)','resultat','s')
arrow(ax,(A[0]+1.5,A[1]+0.5),(T[0]-1.5,T[1]-0.7),'varie',curve=0.3)
arrow(ax,(B[0]+1.5,B[1]),(T[0]-1.2,T[1]+0.9),'varie',curve=-0.2)
text(ax,66,43,'droite','resultat','m')
text(ax,44,5,r'$\det T=0$','encre','l')
save(fig,'76-130')
