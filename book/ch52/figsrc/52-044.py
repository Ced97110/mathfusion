import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
def mat(cx,cy,s,role):
    w,h=5.5,6.2
    for sg in (-1,1):
        x=cx+sg*w; line(ax,[(x-sg*1.2,cy+h),(x,cy+h),(x,cy-h),(x-sg*1.2,cy-h)],role)
    text(ax,cx,cy,s,role,'m')
A='1   1\n0   1'; B='1   0\n1   1'
for cy,l,L,R,P,rl,rr in ((36,r'$ab$',A,B,'2   1\n1   1','sujet','autre'),(14,r'$ba$',B,A,'1   1\n1   2','autre','sujet')):
    text(ax,7,cy,l,'encre','m'); mat(20,cy,L,rl); text(ax,31,cy,'×','encre','m'); mat(42,cy,R,rr); text(ax,53,cy,'=','encre','m'); mat(68,cy,P,'resultat')
text(ax,78,25,'≠','limite','xl'); text(ax,38,3,'l’ordre compte','fixe','s')
save(fig,'52-044')
