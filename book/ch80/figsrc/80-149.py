import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
text(ax,14,50,r'partie $A$','sujet','s'); text(ax,46,50,'neutre','fixe','s'); text(ax,77,50,'résultat','resultat','s')
rows=[(36,r'$\cup$','dash',r'$\emptyset$'),(12,r'$\cap$','full',r'$\{1,2,3\}$')]
for y,op,k,lab in rows:
    box(ax,3,y-6,22,12,'sujet',label=r'$\{1,2\}$')
    text(ax,29,y,op,'encre','l')
    box(ax,33,y-6,26,12,'fixe',label=lab,dash=(k=='dash'),fill=(k!='dash'))
    text(ax,63,y,'=','encre','l')
    box(ax,66,y-6,19,12,'resultat',label=r'$\{1,2\}$',size='s')
save(fig,'80-149')
