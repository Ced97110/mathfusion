import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
# parenthèse ouverte
text(ax,30,52,'(','sujet','l',weight='bold')
arrow(ax,(16,62),(29,55),'fixe',lw=0.6)
text(ax,16,65,'parenthèse ouverte','sujet','s')
# parenthèse fermée
text(ax,50,52,')','sujet','l',weight='bold')
arrow(ax,(70,62),(51,55),'fixe',lw=0.6)
text(ax,70,65,'parenthèse fermée','sujet','s')
# ce qui est entre les deux
text(ax,40,52,'2 + 3','encre','l')
text(ax,60,52,'× 4','encre','l')
brace(ax,33,47,48,'varie',label="d'abord : 5",down=True,size='s')
# résultat
arrow(ax,(40,41),(40,36),'varie')
text(ax,44,32,'5 × 4 = 20','resultat','m')
# sans parenthèses
line(ax,[(6,25),(82,25)],'fixe',lw=0.5)
text(ax,18,16,'sans parenthèses :','fixe','s')
text(ax,60,16,'2 + 3 × 4 = 14','autre','m')
text(ax,60,8,'3 × 4 passe avant','autre','s')
save(fig,'04-049')
