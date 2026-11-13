import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
X=dict(a=12,eq=24,b=36,t=50,r=66)
y1,y2=62,32
def ligne(y,a,b,q,r,ca,cb,cr):
    text(ax,X['a'],y,a,ca,'l'); text(ax,X['eq'],y,'=','encre','l'); text(ax,X['b'],y,b,cb,'l')
    text(ax,X['t'],y,rf'$\times${q} +','encre','l'); text(ax,X['r'],y,r,cr,'l')
ligne(y1,'18','12','1','6','sujet','autre','varie')
ligne(y2,'12','6','2','0','autre','varie','fixe')
arrow(ax,(X['b'],y1-4),(X['a']+2,y2+4),'autre',lw=1.4)
arrow(ax,(X['r'],y1-4),(X['b']+3,y2+4),'varie',lw=1.4)
disc(ax,X['b'],y2,5.2,'resultat',fill=False,lw=1.6)
text(ax,X['b'],y2-9,'PGCD = 6','resultat','m',weight='bold')
text(ax,2,16,'diviseur → nombre divisé','autre','s',ha='left')
text(ax,2,9,'reste → diviseur','varie','s',ha='left')
text(ax,78,y2-9,'reste 0 : fin','fixe','s')
save(fig,'05-095')
