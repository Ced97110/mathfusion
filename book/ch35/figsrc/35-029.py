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
fig,ax=canvas(64)
text(ax,34,56,r'$\sqrt{3^2+4^2}$','sujet','xl'); text(ax,56,56,r'$=\ 5$','resultat','xl')
O,A,Hh=tri(ax,8,8,3,4,6.5,ra='fixe',rb='fixe',rr='resultat')
text(ax,17.5,4.5,r'$a$ = 3','fixe','s'); text(ax,A[0]+1.5,21,r'$b$ = 4','fixe','s',ha='left'); hyp_label(ax,O,Hh,'5','resultat',4)
text(ax,66,38,r'$3^2+4^2$ = 25','sujet','m'); arrow(ax,(66,34),(66,25),'varie'); text(ax,66,21,r'$\sqrt{25}$ = 5','resultat','m')
text(ax,66,10,'hypoténuse = 5','resultat','s')
save(fig,'35-029')
