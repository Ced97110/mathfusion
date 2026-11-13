import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
u=7
for (ox,top,lab,pl,hl) in [(8,(3,4),'(3, 4)',r'$\sqrt{25}=5$',None),(56,(1,1),'(1, 1)',r'$\sqrt{2}$',None)]:
    A=(ox,14);B=(ox+top[0]*u,14);C=(ox+top[0]*u,14+top[1]*u)
    poly(ax,[A,B,C],'sujet'); line(ax,[A,C],'resultat',lw=1.8)
    disc(ax,*A,1.1,'sujet'); disc(ax,*C,1.1,'sujet')
    text(ax,ox,9,'(0, 0)','sujet','s'); text(ax,C[0]+2,C[1]+1,lab,'sujet','s',ha='left')
    text(ax,(A[0]+C[0])/2-3,(A[1]+C[1])/2+4,pl,'resultat','s',ha='right')
text(ax,44,54,'toute distance : une racine','encre','s')
save(fig,'22-152')
