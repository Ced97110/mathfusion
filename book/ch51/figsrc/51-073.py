import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
lines=[(r'$(1+2i)(3+i)$','sujet'),(r'$3+i+6i+2i^2$','sujet'),(r'$3+i+6i-2$','sujet'),(r'$(3-2)+(1+6)i$','sujet'),(r'$1+7i$','resultat')]
acts=['on développe','$i^2=-1$','on regroupe','']
ys=[74,58,42,26,10]
for (t,r),y in zip(lines,ys):
    box(ax,16,y-4.5,56,9,r,label=t,size='l')
for a,y0,y1 in zip(acts[:3],ys[:3],ys[1:4]):
    arrow(ax,(44,y0-5),(44,y1+5),'varie'); text(ax,50,(y0+y1)/2,a,'varie','s',ha='left')
arrow(ax,(44,ys[3]-5),(44,ys[4]+5),'resultat'); text(ax,50,18,'on calcule','resultat','s',ha='left')
save(fig,'51-073')
