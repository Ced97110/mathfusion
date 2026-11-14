import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,64,r'$x\mapsto 2^x$','varie','l'); text(ax,8,53+10,'addition','sujet','s',ha='left'); text(ax,8,4,'multiplication','resultat','s',ha='left')
for x,v,r in [(14,'3','sujet'),(44,'2','sujet'),(74,'5','sujet')]:
    pass
xs=[16,44,72]
text(ax,30,53,'+','sujet','l'); text(ax,58,53,'=','sujet','l')
text(ax,30,17,r'$\times$','resultat','l'); text(ax,58,17,'=','resultat','l')
for x,a,b in zip(xs,['3','2','5'],['8','4','32']):
    box(ax,x-8,46,16,14,'sujet',label=a,size='l')
    box(ax,x-8,10,16,14,'resultat',label=b,size='l')
    arrow(ax,(x,45),(x,25),'varie')

save(fig,'45-035')
