import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def dot(ax,x,y,role='fixe',r=0.9): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=4))
def wr(ax,pts,role='fixe',dash=False): line(ax,pts,role,lw=1.2,dash=dash)
def sw(ax,x,y,closed,role='fixe',L=10):
    dot(ax,x,y,role); dot(ax,x+L,y,role)
    wr(ax,[(x,y),(x+L,y)] if closed else [(x,y),(x+L-1.5,y+4.5)],role)
def ser(ax,x,y,ca,cb,role=None,L=9):
    xa=x+5; xb=xa+L+6; e=xb+L+5
    r=role or ('resultat' if (ca and cb) else 'fixe')
    wr(ax,[(x,y),(xa,y)],r); sw(ax,xa,y,ca,r,L); wr(ax,[(xa+L,y),(xb,y)],r); sw(ax,xb,y,cb,r,L); wr(ax,[(xb+L,y),(e,y)],r)
    return e
def par(ax,x,y,ca,cb,W=26,L=8,h=5,st=3,letters=False,role=None):
    sx=x+W/2-L/2; xv=x+st; xw=x+W-st
    ra=role or ('resultat' if ca else 'fixe'); rb=role or ('resultat' if cb else 'fixe'); rs=role or ('resultat' if (ca or cb) else 'fixe')
    wr(ax,[(x,y),(xv,y)],rs); wr(ax,[(xw,y),(x+W,y)],rs)
    for yy,c,r in ((y+h,ca,ra),(y-h,cb,rb)):
        wr(ax,[(xv,y),(xv,yy),(sx,yy)],r); sw(ax,sx,yy,c,r,L); wr(ax,[(sx+L,yy),(xw,yy),(xw,y)],r)
    if letters:
        text(ax,sx+L/2,y+h+8,r'$a$','sujet','s'); text(ax,sx+L/2,y-h-4.5,r'$b$','sujet','s')
fig,ax=canvas(64)
box(ax,3,36,14,12,'fixe',label='pile',size='s'); wr(ax,[(17,42),(30,42)],'fixe')
sw(ax,30,42,True,'sujet',L=14); wr(ax,[(44,42),(58,42)],'fixe')
disc(ax,64,42,5,'fixe'); text(ax,64,33,'lampe','fixe','s')
text(ax,37,53,'interrupteur','sujet','m')
text(ax,44,25,'deux états :','varie','s')
sw(ax,8,14,True,'resultat',L=14); text(ax,15,6,'fermé','resultat','m')
sw(ax,60,14,False,'fixe',L=14); text(ax,67,6,'ouvert','fixe','m')
arrow(ax,(25,14),(35,14),'varie',both=True); arrow(ax,(53,14),(43,14),'varie',both=True)
save(fig,'80-157')
