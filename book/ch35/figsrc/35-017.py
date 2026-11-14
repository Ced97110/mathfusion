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
fig,ax=canvas(80)
text(ax,44,75,r'$R=\sqrt{a^2+b^2}$','sujet','l')
text(ax,24,66,r'$a$ = 5','fixe','s'); text(ax,64,66,r'$b$ = 12','fixe','s')
box(ax,6,48,36,12,'sujet',label=r'1. $5^2$ = 25')
box(ax,46,48,36,12,'sujet',label=r'2. $12^2$ = 144')
box(ax,16,26,56,12,'varie',label='3. 25 + 144 = 169')
box(ax,16,4,56,12,'resultat',label=r'4. $\sqrt{169}$ = 13',weight='bold')
arrow(ax,(24,48),(36,38),'varie'); arrow(ax,(64,48),(52,38),'varie'); arrow(ax,(44,26),(44,16),'varie')
save(fig,'35-017')
