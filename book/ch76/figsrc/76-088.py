import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
for i,n in enumerate('1234'):
    disc(ax,25+i*13,54,5,'sujet',label=n,size='l')
text(ax,3,54,r'$n=4$','sujet','m',ha='left')
text(ax,44,41,'parties à 2 éléments','varie','m')
parts=['12','13','14','23','24','34']
for i,p in enumerate(parts):
    box(ax,14+(i%3)*22,24-(i//3)*12,16,9,'varie',label=p,size='m')
text(ax,44,5,r'$\binom{4}{2}=6$','resultat','xl')
save(fig,'76-088')
