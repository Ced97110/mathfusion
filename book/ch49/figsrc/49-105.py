import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
box(ax,2,3,84,60,'sujet',fill=False,lw=1.2)
text(ax,44,57,r'$\mathrm{Sym}\,S$','sujet','l',weight='bold')
text(ax,44,49,'images de 1, 2, 3 (6 façons)','fixe','s')
perms=['1 2 3','1 3 2','2 1 3','2 3 1','3 1 2','3 2 1']
for k,p in enumerate(perms):
    r,c=divmod(k,3)
    box(ax,8+c*25,26-r*14,22,10,'resultat' if k==0 else 'fixe',label=p)
save(fig,'49-105')
