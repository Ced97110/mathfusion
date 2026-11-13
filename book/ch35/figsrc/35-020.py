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
fig,ax=canvas(78)
text(ax,44,73,r'$\tan\alpha=b/a$','sujet','l')
ox,oy,s=10,22,5
O,A,Hh=tri(ax,ox,oy,3,4,s,ra='sujet',rb='sujet',rr='sujet')
O2,A2,H2=tri(ax,ox,oy,6,8,s,ra='autre',rb='autre',rr='autre')
line(ax,[O,Hh],'sujet',lw=1.8)
brace(ax,ox,ox+15,oy-3,'sujet',r'$a$ = 3'); brace(ax,ox,ox+30,oy-11,'autre',r'$a$ = 6')
text(ax,ox+15+1.5,oy+10,r'$b$ = 4','sujet','s',ha='left'); text(ax,ox+30+1.5,oy+30,r'$b$ = 8','autre','s',ha='left')
hyp_label(ax,O,Hh,r'$R$ = 5','sujet',5.5); hyp_label(ax,Hh,H2,r'$R$ = 10','autre',5.5)
text(ax,68,32,'4/3 ≈ 1,333','sujet','m'); text(ax,68,22,'8/6 ≈ 1,333','autre','m')
save(fig,'35-020')
