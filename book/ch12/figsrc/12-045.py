import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,'le contraire change le verdict','encre','m')
cols=[(r'$6>4$',r'$6\leq4$'),(r'$4=4$',r'$4\neq4$'),(r'$4<6$',r'$4\geq6$')]
for i,(a,b) in enumerate(cols):
    x=3+i*28.5
    box(ax,x,26,25,13,'resultat',label=a,size='l'); text(ax,x+12.5,21.5,'vrai','resultat','s')
    box(ax,x,3,25,13,'limite',label=b,size='l')
    arrow(ax,(x+12.5,20),(x+12.5,17),'varie')
save(fig,'12-045')
