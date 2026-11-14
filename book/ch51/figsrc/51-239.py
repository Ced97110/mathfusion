import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def motif(k,c,y):
    if k==1:
        disc(ax,c-7,y,2.2,"fixe"); arrow(ax,(c-4.4,y),(c+4.4,y),"limite",lw=1.0); disc(ax,c+7,y,2.2,"limite",fill=False)
    elif k==2:
        disc(ax,c-7,y+3.5,2.2,"fixe"); disc(ax,c-7,y-3.5,2.2,"fixe"); disc(ax,c+7,y,2.2,"fixe")
        arrow(ax,(c-4.6,y+3.2),(c+4.6,y+0.5),"limite",lw=1.0); arrow(ax,(c-4.6,y-3.2),(c+4.6,y-0.5),"limite",lw=1.0)
    else:
        disc(ax,c-8,y,2.2,"fixe"); disc(ax,c,y,2.2,"fixe"); disc(ax,c+8,y,2.2,"limite",fill=False)
text(ax,44,76,'cadran à 6 : ×2','fixe','m')
rows=[('étape 1 échoue',r'$2\times3=6=0$'),('étape 2 échoue',r'$2\times1=2\times4=2$'),('étape 3 échoue','arrivées 0, 2, 4 : pas 1')]
ys=[52,30,8]
for k,((a,b),y) in enumerate(zip(rows,ys)):
    box(ax,3,y,24,14,'limite',label=None,lw=2.0 if k==0 else 0.8); text(ax,15,y+7,a,'limite','s',weight='bold')
    text(ax,31,y+7,b,'encre','m',ha='left')
    motif(k+1,77,y+7)
for y in ys[:2]: arrow(ax,(15,y-0.3),(15,y-7.5),'varie',lw=1.2)
save(fig,'51-239')
