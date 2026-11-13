import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
labs=[(64,'(3) est maximal','sujet'),(46,r'$\mathbb{Z}/3\mathbb{Z}$ est un corps','autre'),(28,r'$\mathbb{Z}/3\mathbb{Z}$ est un domaine','autre'),(10,'(3) est premier','resultat')]
for y,l,r in labs:
    box(ax,3,y,46,9,r,label=l,size='s')
for y in (64,46,28):
    arrow(ax,(26,y),(26,y-9),'varie')
arrow(ax,(50,32.5),(55,32.5),'fixe')
text(ax,71,43,'classes non nulles','fixe','s')
for dy,t in zip((38,32.5,27),('1 × 1 = 1','1 × 2 = 2','2 × 2 = 1')):
    text(ax,71,dy,t,'encre','s')
text(ax,71,21,'jamais 0','resultat','s')
save(fig,'52-104')
