import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,22,53,"l'ordre ne compte pas",'resultat','s'); text(ax,66,53,"l'ordre compte",'limite','s')
rows=[(44,(r'$A\cap B$',r'$B\cap A$'),(r'$\{2\}$',r'$\{2\}$'),(r'$A\setminus B$',r'$B\setminus A$'),(r'$\{1\}$',r'$\{3\}$')),]
for (c,ex,re,role,rr,sg,rs) in ((22,(r'$A\cap B$',r'$B\cap A$'),(r'$\{2\}$',r'$\{2\}$'),'sujet','resultat',r'$=$','resultat'),(66,(r'$A\setminus B$',r'$B\setminus A$'),(r'$\{1\}$',r'$\{3\}$'),'varie','limite',r'$\neq$','limite')):
    for y,e,r_ in zip((42,16),ex,re):
        box(ax,c-20,y-5,18,10,role,label=e,size='s'); arrow(ax,(c-1,y),(c+3,y),role)
        box(ax,c+4,y-5,14,10,rr,label=r_,size='s')
    text(ax,c,29,sg,rs,'xl')
save(fig,'42-149')
