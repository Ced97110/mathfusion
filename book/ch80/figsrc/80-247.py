import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
text(ax,22,82,'diviseurs de 30','encre','s')
text(ax,69,82,'atomes sous eux','encre','s')
rows=[(62,'6','sujet','{2, 3}'),(44,'10','autre','{2, 5}'),(26,'PPCM(6, 10) = 30','resultat','∪ : {2, 3, 5}'),(8,'PGCD(6, 10) = 2','resultat','∩ : {2}')]
for y,a,rl,b in rows:
    box(ax,2,y,40,12,rl,label=a,size='s'); box(ax,52,y,34,12,rl,label=b,size='s')
    arrow(ax,(42.5,y+6),(51.5,y+6),'varie')
text(ax,47,73,r'$\varphi$','varie','m')
save(fig,'80-247')
