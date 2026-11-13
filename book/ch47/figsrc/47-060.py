import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
box(ax,2,28,84,42,'fixe',fill=False)
text(ax,44,76,r'$S_3$ : 6 permutations','fixe','m')
box(ax,3.8,54,53.8,13,'sujet',fill=False,dash=True)
items=[(17,60,r'$1$','sujet'),(44,60,r'$(1\,2)$','sujet'),(71,60,r'$(1\,3)$','fixe'),
       (17,40,r'$(2\,3)$','fixe'),(44,40,r'$(1\,2\,3)$','fixe'),(71,40,r'$(1\,3\,2)$','fixe')]
for cx,cy,l,r in items: box(ax,cx-11,cy-4.5,22,9,r,label=l,size='s')
text(ax,30.7,50,r'$K$ : 2 éléments','sujet','s')
text(ax,44,16,r'$(1\,2)(1\,2)=1$','resultat','l')
text(ax,44,7,'deux échanges = identité','resultat','s')
save(fig,'47-060')
