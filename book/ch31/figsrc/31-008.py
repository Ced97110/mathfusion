import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def eq(x,y,w=10):
    line(ax,[(x,y+1),(x+w,y+1)],'encre'); line(ax,[(x,y-1),(x+w,y-1)],'encre')
def times(x,y):
    line(ax,[(x-2,y-2),(x+2,y+2)],'encre'); line(ax,[(x-2,y+2),(x+2,y-2)],'encre')
text(ax,26,54,r'$1+\tan^2\theta$','sujet','m'); text(ax,52,54,r'$1-\sin^2\theta$','varie','m'); text(ax,77,54,'produit','resultat','m')
for i,(an,a,b) in enumerate([('35°','1,4903','0,6710'),('60°','4','0,25')]):
    y=32-i*18
    text(ax,6,y+5,an,'encre','l')
    box(ax,16,y,20,10,'sujet',label=a,size='m'); times(39.5,y+5)
    box(ax,43,y,20,10,'varie',label=b,size='m'); 
    line(ax,[(66,y+6),(70,y+6)],'encre'); line(ax,[(66,y+4),(70,y+4)],'encre')
    box(ax,72,y,14,10,'resultat',label='1',size='l')
text(ax,44,6,'Deux essais : pas une preuve','fixe','m')
save(fig,'31-008')
