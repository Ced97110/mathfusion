import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,4,72,'4 fois 6 redonne 24','fixe','m',ha='left'); text(ax,4,66,'6 fois 3 redonne 18','fixe','m',ha='left')
text(ax,52,69,'une phrase par cas','fixe','s',ha='left')
arrow(ax,(20,61),(20,52),'varie')
text(ax,20,46,'n','sujet','l',weight='bold',style='italic'); text(ax,25,46,r'= $d$ × $q$','encre','l',ha='left')
text(ax,58,46,'une ligne pour tous','encre','s',ha='left')
for y,n,f in [(37,'24','= 4 × 6'),(30,'18','= 6 × 3'),(23,'90','= 15 × 6')]:
    text(ax,20,y,n,'sujet','m'); text(ax,25,y,f,'encre','m',ha='left')
box(ax,16,19,8,31,'sujet',fill=False,dash=True)
text(ax,20,15,'n : le nombre partagé','sujet','s')
save(fig,'03-037')
