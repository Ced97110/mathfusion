import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,66,r'$u=100$ et $v=010$','encre','m')
x0=30; y0=8; cw=24; ch=17
for j,(b) in enumerate((0,1)):
    text(ax,x0+j*cw+cw/2,y0+2*ch+4,r'$%d\times100$'%j,'sujet','s')
    text(ax,x0-3,y0+ (1-j)*ch+ch/2 ,r'$%d\times010$'%j,'autre','s',ha='right')
for a in (0,1):
    for b in (0,1):
        lab=f'{a}{b}0'
        box(ax,x0+a*cw+1,y0+(1-b)*ch+1,cw-2,ch-2,'sujet',label=lab,size='l')
text(ax,x0+cw,y0-3.5,'plan vectoriel : 4 étiquettes','sujet','s')
save(fig,'80-050')
