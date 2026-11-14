import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
for y,a,n,par,res,role in [(30,'3 1 2','2 échanges','pair','+1','resultat'),(8,'2 1 3','1 échange','impair','−1','varie')]:
    box(ax,3,y,17,12,'sujet',label=a,size='l'); arrow(ax,(21,y+6),(38,y+6),'varie')
    text(ax,29.5,y+10.5,n,'varie','s'); text(ax,29.5,y+1.5,par,'varie','s')
    box(ax,39,y,17,12,'fixe',label='1 2 3',size='l')
    text(ax,60,y+6,r'$sg(\sigma)=$'+res.replace('−','-'),role,'m',ha='left')
save(fig,'76-095')
