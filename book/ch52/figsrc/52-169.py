import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,2,34,40,40,'fixe'); text(ax,22,70,'R','fixe','m')
box(ax,46,34,40,40,'fixe'); text(ax,66,70,'R/I','fixe','m')
box(ax,7,40,30,16,'sujet',label='S',size='m')
box(ax,51,40,30,16,'resultat',label='(S + I)/I',size='m')
arrow(ax,(37,48),(51,48),'varie'); text(ax,44,52.5,'ν|S','varie','s')
arrow(ax,(44,74.8),(44,74.8),'fixe') if False else None
brace(ax,7,37,40,'varie',label='noyau : S ∩ I',down=True,depth=2.4)
text(ax,44,16,'S/(S ∩ I) ≅ (S + I)/I','resultat','m')
text(ax,44,8,'théorème fondamental','fixe','s')
save(fig,'52-169')
