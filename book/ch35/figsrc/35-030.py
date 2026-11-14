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
fig,ax=canvas(70)
text(ax,44,66,r'$a/R$ : cosinus de $\alpha$','sujet','l')
O,A,Hh=tri(ax,6,32,3,4,6,ra='sujet',rb='fixe',rr='fixe')
arc(ax,O,4,0,53.13); text(ax,O[0]+7,34.5,r'$\alpha$','varie','s'); hyp_label(ax,O,Hh,r'$R$ = 5','fixe',4.5)
box(ax,6,16,30,5,'fixe',label=None); box(ax,6,8,18,5,'sujet')
text(ax,38,18.5,r'$R$ = 5','fixe','s',ha='left'); text(ax,26,10.5,r'$a$ = 3','sujet','s',ha='left')
text(ax,66,50,r'$\frac{a}{R}$','sujet','xl'); text(ax,66,36,r'$\frac{3}{5}=0{,}6$','resultat','m'); text(ax,66,24,r'$=\cos\alpha$','varie','m')
save(fig,'35-030')
