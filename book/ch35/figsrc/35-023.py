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
fig,ax=canvas(62)
y0,A=30,3.5; X=lambda d: 8+72*d/360
line(ax,[(8,y0),(80,y0)],'fixe',lw=0.6)
wave(ax,8,80,y0,5*A,0,'fixe',dash=True); wave(ax,8,80,y0,5*A,53.13,'sujet',lw=1.6)
line(ax,[(X(36.87),y0),(X(36.87),y0+5*A)],'sujet',dash=True); line(ax,[(X(90),y0),(X(90),y0+5*A)],'fixe',dash=True)
text(ax,X(36.87),y0-4,'36,87°','sujet','s'); text(ax,X(90),y0-4,'90°','fixe','s')
arrow(ax,(X(90),y0+5*A+3),(X(36.87),y0+5*A+3),'varie'); text(ax,X(63),y0+5*A+7,r'$\alpha$ = 53,13°','varie','m')
text(ax,6,y0+2.5*A,r'$R$ = 5','sujet','s',ha='center')
brace(ax,8,80,12,'fixe','période 360°')
line(ax,[(54,52),(60,52)],'fixe',dash=True); text(ax,61,52,r'$\sin x$','fixe','s',ha='left')
line(ax,[(54,57),(60,57)],'sujet',lw=1.6); text(ax,61,57,'l’onde','sujet','s',ha='left')
save(fig,'35-023')
