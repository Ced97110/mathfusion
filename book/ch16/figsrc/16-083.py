import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def ligne(y,role,res,note):
    text(ax,8,y,'$3$','varie','xl'); text(ax,16,y,r'$(m\,-\,6)$','encre','xl',ha='left')
    text(ax,60,y,res,role,'xl',ha='left'); text(ax,60,y-9,note,role,'s',ha='left')
ligne(62,'limite',r'$3m-6$','6 oublié : faux')
ligne(26,'resultat',r'$3m-18$','tout multiplié : juste')
arrow(ax,(9,67),(18,67),'limite',curve=-0.5); text(ax,31,52,'$6$ non multiplié','limite','s')
arrow(ax,(9,31),(18,31),'resultat',curve=-0.5); arrow(ax,(9,31),(28,31),'resultat',curve=-0.5)
text(ax,31,14,'$m$ et $6$ multipliés','resultat','s')
save(fig,'16-083')
