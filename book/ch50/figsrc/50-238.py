import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,44,60,r'$|G|=12$ : une case par élément','encre','s')
rows=[(r'$p=2$ : $2^2=4$ éléments',4,'sujet',44),(r'$p=3$ : $3^1=3$ éléments',3,'sujet',26),(r'$p=5$ : $5^0=1$ : juste $\{e\}$',1,'varie',8)]
for lab,k,role,y in rows:
    text(ax,8,y+10,lab,role,'s',ha='left')
    for i in range(12):
        box(ax,8+6*i,y,5.6,5.6,role if i<k else 'fixe',r=0.3,lw=0.6)
text(ax,8+2.8,8+2.8,r'$e$','varie','s')
save(fig,'50-238')
