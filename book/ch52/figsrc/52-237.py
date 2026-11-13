import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
box(ax,16,60,4,4,'fixe',lw=0.5,r=0.3); text(ax,22,62,'signe','fixe','s',ha='left')
box(ax,44,60,4,4,'sujet',lw=0.5,r=0.3); text(ax,50,62,'bits du nombre','sujet','s',ha='left')
for y,n,lab,res in ((42,3,'4 bits',r'$2^{3}-1=7$'),(28,7,'8 bits',r'$2^{7}-1=127$')):
    box(ax,18,y,4,8,'fixe',lw=0.5,r=0.3)
    for i in range(n): box(ax,22+i*4,y,4,8,'sujet',lw=0.5,r=0.3)
    text(ax,1,y+4,lab,'encre','m',ha='left'); text(ax,56,y+4,res,'resultat','s',ha='left')
box(ax,18,14,4,8,'fixe',lw=0.5,r=0.3); box(ax,22,14,28,8,'sujet',lw=0.5,r=0.5,label='63 bits',size='s')
text(ax,1,18,'64 bits','encre','m',ha='left'); text(ax,56,18,r'$2^{63}-1$','resultat','s',ha='left')
text(ax,44,6,'= 9 223 372 036 854 775 807','resultat','s')
save(fig,'52-237')
