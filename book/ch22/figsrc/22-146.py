import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
f=numberline(ax,6,70,32,-4,4,step=1,every=4,arrow_right=False)
box(ax,3,22,f(0)-4,18,'limite',fill=False,dash=True)
text(ax,f(-2),37,'interdit','limite','s')
disc(ax,f(-2),32,1.8,'limite',fill=False,lw=1.2)
text(ax,f(-2),19,'√4 n’est pas −2','limite','s')
for v,l in [(0,r'$\sqrt{0}$'),(3,r'$\sqrt{9}$'),(2**0.5,r'$\sqrt{2}$')]:
    r=v if v!=3 else 3
    disc(ax,f(r),32,1.6,'resultat'); text(ax,f(r),38,l,'resultat','s')
save(fig,'22-146')
