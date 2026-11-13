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
box(ax,19,60,50,12,'limite',label=r'dans ℤ/6 : $2\times3=0$',weight='bold')
xs=[2,31,60]; spec=[('étape 1','flèche sur 0'),('étape 2',r'1 et 4 $\to$ 2'),('étape 3','1 non atteint')]
for k,(x,(a,b)) in enumerate(zip(xs,spec)):
    c=x+13.25
    arrow(ax,(44,59.6),(c,46.6),'limite',lw=1.2)
    box(ax,x,28,26.5,18,'limite'); text(ax,c,40.5,a,'limite','m',weight='bold'); text(ax,c,33,b,'limite','s')
    motif(k+1,c,16)
save(fig,'51-237')
