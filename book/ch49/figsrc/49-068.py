import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,16,60,56,12,'sujet',label=r'$srs = r^{-1}$',size='l')
arrow(ax,(44,59),(44,52),'varie'); text(ax,66,55.5,r'× $r$ à gauche','varie','s')
box(ax,10,38,68,12,'fixe',label=r'$r\,srs = r\,r^{-1}$',size='l')
arrow(ax,(44,37),(44,30),'varie'); text(ax,67,33.5,r'$r\,r^{-1}=1$','varie','s')
box(ax,16,16,56,12,'resultat',label=r'$rsrs = 1$',size='l')
arrow(ax,(8,22),(8,66),'autre',curve=-0.0,both=True); text(ax,22,8,'même relation, deux écritures','autre','s')
save(fig,'49-068')
