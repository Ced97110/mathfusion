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
fig,ax=canvas(66)
for y,c,lab,v,r in ((54,True,'fermé','1','resultat'),(36,False,'ouvert','0','fixe')):
    sw(ax,6,y,c,r,L=14); text(ax,13,y-6.5,lab,r,'s')
    arrow(ax,(26,y),(40,y),'varie'); box(ax,44,y-6,14,12,r,label=v,size='l')
sw(ax,6,14,True,'resultat',L=12); sw(ax,26,14,False,'fixe',L=12)
text(ax,12,7,r'$a$','sujet','s'); text(ax,32,7,r'$b$','sujet','s')
arrow(ax,(42,14),(52,14),'varie'); box(ax,54,8,28,12,'sujet',label=r'$(1,\ 0)$')
text(ax,22,24,'une position','fixe','s')
save(fig,'80-166')
