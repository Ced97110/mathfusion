import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
box(ax,2,72,40,12,'sujet',label='le plus grand',size='m')
text(ax,22,67.5,'diviseur commun','sujet','s')
box(ax,2,16,40,12,'autre',label='divisible par tous',size='s')
text(ax,22,11.5,'les diviseurs communs','autre','s')
# sens 1 : de "divisible par tous" vers "le plus grand"
arrow(ax,(8,31),(8,64),'sujet',lw=1.4)
text(ax,12,58,'sens 1 (vers le haut)','sujet','s',ha='left')
text(ax,12,53,r"$d'\mid d\ \Rightarrow\ d'\leq d$",'sujet','s',ha='left')
# sens 2 : de "le plus grand" vers "divisible par tous"
arrow(ax,(36,64),(36,31),'varie',lw=1.4)
text(ax,46,47,'sens 2 (vers le bas)','varie','s',ha='left')
text(ax,46,42,'grâce à Bézout :','varie','s',ha='left')
text(ax,46,37,r"$d'\mid au+bv=d$",'varie','s',ha='left')
text(ax,46,32,r'($u$, $v$ entiers)','varie','s',ha='left')
text(ax,46,24,r"$d'$ : un diviseur commun",'autre','s',ha='left')
text(ax,44,3,'pour 12 et 18 : les deux = 6','resultat','s')
save(fig,'05-110')
