import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66); s=8; o=(20,34)
pl=lambda x,y:(o[0]+s*x,o[1]+s*y)
line(ax,[pl(0,-3.5),pl(0,3.5)],'fixe',lw=0.5); line(ax,[pl(-2.2,0),pl(3.6,0)],'sujet',lw=1.5)
disc(ax,*pl(3,2),1.2,'encre'); disc(ax,*pl(3,-2),1.2,'varie')
arrow(ax,(pl(3,2)[0],pl(3,2)[1]-2),(pl(3,-2)[0],pl(3,-2)[1]+2),'varie',lw=1.2)
text(ax,pl(3,2)[0],pl(3,2)[1]+4,'(3 ; 2)','encre','s'); text(ax,pl(3,-2)[0],pl(3,-2)[1]-4,'(3 ; −2)','varie','s')
text(ax,pl(-2.2,0)[0]-1,pl(0,0)[1]+4,'axe horizontal','sujet','s',ha='left')
cells=[('1','sujet'),('0','fixe'),('0','fixe'),('−1','varie')]
for i,(l,r) in enumerate(cells):
    c,rw=i%2,i//2; box(ax,64+c*10,46-rw*10,10,10,r,label=l)
text(ax,59,46,r'$\tau$ =','sujet','l')
text(ax,75,27,'1 : garde $x$','sujet','s'); text(ax,75,20,'−1 : change le\nsigne de y','varie','s')
save(fig,'73-101')
