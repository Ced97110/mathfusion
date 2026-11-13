import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
for y,l,r in ((66,r'$2y-1\leq 16$','sujet'),(38,r'$2y\leq 17$','sujet'),(10,r'$y\leq 8{,}5$','resultat')):
    box(ax,8,y,36,12,r,label=l,size='l')
arrow(ax,(26,64),(26,52),'varie'); text(ax,30,58,'+ 1 des deux côtés','varie','s',ha='left')
arrow(ax,(26,36),(26,24),'varie'); text(ax,30,30,'÷ 2 des deux côtés','varie','s',ha='left')
text(ax,48,16,'on s\'arrête ici','resultat','s',ha='left')
save(fig,'17-077')
