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
fig,ax=canvas(66)
text(ax,44,62,r'$\cos\alpha=a/R$','sujet','l')
for (ox,a,b,s,R,res,ang) in [(8,3,4,7,5,'3/5 = 0,6','53,13°'),(50,5,12,3,13,'5/13 ≈ 0,3846','67,38°')]:
    O,A,Hh=tri(ax,ox,20,a,b,s)
    text(ax,(O[0]+A[0])/2,16,f'$a$ = {a}','sujet','s')
    hyp_label(ax,O,Hh,f'$R$ = {R}','fixe',6)
    arc(ax,O,4,0,math.degrees(math.atan2(b,a)))
    text(ax,O[0]+7,22.5 if a==3 else 23.5,r'$\alpha$','varie','s')
    text(ax,(O[0]+A[0])/2+2,9,res,'resultat','s'); text(ax,(O[0]+A[0])/2+2,3.5,'α = '+ang,'varie','s')
save(fig,'35-018')
