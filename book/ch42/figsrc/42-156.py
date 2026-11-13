import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np, matplotlib.colors as mc
fig,ax=canvas(62)
N=400; ys,xs=np.mgrid[0:1:N*0.7j,0:1:N*1j]
def panel(x0,y0,w,h,mode):
    X=x0+xs*w; Y=y0+ys*h
    ca=(x0+0.38*w,y0+0.5*h); cb=(x0+0.62*w,y0+0.5*h); r=0.27*h
    inA=(X-ca[0])**2+(Y-ca[1])**2<r*r; inB=(X-cb[0])**2+(Y-cb[1])**2<r*r
    img=np.ones((xs.shape[0],xs.shape[1],3))
    g=np.array(mc.to_rgb(FILL['resultat'])); b=np.array(mc.to_rgb(FILL['sujet'])); o=np.array(mc.to_rgb(FILL['varie']))
    if mode==0: img[~inA&~inB]=g
    else:
        img[~inA]=b; img[~inB]=o; img[~inA&~inB]=(b+o)/2*0.9
    ax.imshow(img,extent=(x0,x0+w,y0,y0+h),origin='lower',zorder=1,interpolation='nearest',aspect='equal')
    box(ax,x0,y0,w,h,'fixe',fill=False)
    for c,l,role in ((ca,'A','sujet'),(cb,'B','varie')):
        disc(ax,c[0],c[1],r,role,fill=False,lw=1.1)
    text(ax,ca[0]-0.12*w,y0+0.5*h+r+3,'A','sujet','m'); text(ax,cb[0]+0.12*w,y0+0.5*h+r+3,'B','varie','m')
    text(ax,x0+4,y0+h-3.5,'U','fixe','s')
panel(2,22,38,30,0); panel(48,22,38,30,1)
text(ax,44,37,'=','resultat','xl')
text(ax,21,17,r'$(A\cup B)^\prime$','resultat','m'); text(ax,67,17,r'$A^\prime\cap B^\prime$','resultat','m')
text(ax,21,9,'vert : hors des deux disques','resultat','s'); text(ax,67,9,'bleu + orange : se superposent','encre','s')
ax.set_xlim(0,88); ax.set_ylim(0,62)
save(fig,'42-156')
