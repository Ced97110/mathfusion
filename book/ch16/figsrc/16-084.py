import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
rows=[(79,r'$3(m-6)-2m=-3$','sujet',''),(60,r'$3m-18-2m=-3$','varie','distribuer'),(41,r'$m-18=-3$','varie','regrouper'),(22,r'$m=15$','resultat','ajouter 18')]
for i,(y,s,r,l) in enumerate(rows):
    box(ax,8,y-5,46,10,r,label=s,size='m')
    if l: text(ax,58,y+9.5,l,'varie','s',ha='left'); arrow(ax,(31,y+14),(31,y+5.5),'varie')
text(ax,44,7,r'$3\times 9=27,\ 27-30=-3$','resultat','m')
save(fig,'16-084')
