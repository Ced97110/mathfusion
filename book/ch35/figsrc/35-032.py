import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
def tri(ax,ox,oy,a,b,s,ra='sujet',rb='fixe',rr='fixe'):
    O=(ox,oy);A=(ox+a*s,oy);H=(ox+a*s,oy+b*s)
    poly(ax,[O,A,H],'fixe')
    line(ax,[O,A],ra,lw=1.8);line(ax,[A,H],rb,lw=1.8);line(ax,[O,H],rr,lw=1.8)
    line(ax,[(A[0]-1.6,oy),(A[0]-1.6,oy+1.6),(A[0],oy+1.6)],'fixe',lw=0.7)
    return O,A,H
def arc(ax,c,r,a0,a1,role='varie'):
    t=np.radians(np.linspace(a0,a1,40)); ax.plot(c[0]+r*np.cos(t),c[1]+r*np.sin(t),color=COL[role],lw=1.2,zorder=4)
def hyp_label(ax,O,H,s,role,off=4.5):
    mx,my=(O[0]+H[0])/2,(O[1]+H[1])/2; dx,dy=H[0]-O[0],H[1]-O[1]; L=math.hypot(dx,dy)
    text(ax,mx-dy/L*off,my+dx/L*off,s,role,'s')
def wave(ax,x0,x1,y,amp,deg0=0,role='sujet',lw=1.3,dash=False):
    d=np.linspace(0,360,120); ax.plot(x0+(x1-x0)*d/360,y+amp*np.sin(np.radians(d+deg0)),color=COL[role],lw=lw,ls='--' if dash else '-',zorder=3)
fig,ax=canvas(112)
box(ax,3,90,82,16,'sujet',label=r'$\sin(x+\alpha)=\cos\alpha\,\sin x+\sin\alpha\,\cos x$',size='s')
arrow(ax,(44,90),(44,80),'varie'); text(ax,50,85,'1. × R','varie','s',ha='left')
box(ax,3,62,82,16,'fixe',label=r'$R\sin(x+\alpha)=R\cos\alpha\,\sin x+R\sin\alpha\,\cos x$',size='s')
arrow(ax,(44,62),(44,52),'varie'); text(ax,50,57,'2. lire les nombres','varie','s',ha='left')
box(ax,3,4,82,46,'resultat')
text(ax,44,43,'3. poser (décisif)','resultat','m',weight='bold')
text(ax,44,34,r'$R\cos\alpha=a$  et  $R\sin\alpha=b$','resultat','m')
text(ax,44,25,r'$5\times0{,}6=3=a$  et  $5\times0{,}8=4=b$','resultat','s')
text(ax,44,12,r'$a\sin x+b\cos x=R\sin(x+\alpha)$','resultat','m')
save(fig,'35-032')
