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
fig,ax=canvas(58)
par(ax,5,28,True,True,W=78,L=12,h=10,st=9,letters=False,role='sujet')
dot(ax,5,28,'sujet',1.5); dot(ax,83,28,'sujet',1.5)
text(ax,44,40.5,r'$a$','sujet','m'); text(ax,44,15.5,r'$b$','sujet','m')
text(ax,44,28,'deux chemins','varie','s')
text(ax,7,35,'départ','fixe','s'); text(ax,81,35,'arrivée','fixe','s')
save(fig,'80-163')
