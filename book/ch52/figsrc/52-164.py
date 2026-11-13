import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
g=16; ox,oy=18,12
for i in range(3):
    line(ax,[(ox,oy+i*g),(ox+2*g,oy+i*g)],'fixe',lw=0.4,dash=True)
    line(ax,[(ox+i*g,oy),(ox+i*g,oy+2*g)],'fixe',lw=0.4,dash=True)
    text(ax,ox+i*g,oy-3.5,str(5*i),'fixe','s')
    text(ax,ox-4,oy+i*g,str(5*i),'fixe','s')
for i in range(3):
    disc(ax,ox+i*g,oy+i*g,1.8,'sujet')
disc(ax,ox+g,oy,1.8,'limite')
arrow(ax,(ox+g,oy+g-2.4),(ox+g,oy+2.4),'varie')
text(ax,ox+g+15,oy+g*0.5,'× (1, 0)','varie','s')
text(ax,ox+g-11,oy+g+3.5,'(5, 5)','sujet','s')
text(ax,ox+g+4,oy+3.6,'(5, 0) : hors image','limite','s',ha='left')
text(ax,44,70,'image de 5ℤ : pas un idéal','limite','m')
text(ax,44,62,'η(n) = (n, n) : pas surjective','sujet','s')
save(fig,'52-164')
