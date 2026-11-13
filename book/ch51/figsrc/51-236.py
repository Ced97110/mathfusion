import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
box(ax,3,38,22,12,'sujet',label=r'$p$ premier'); box(ax,33,38,22,12,'sujet',label='ℤ/p intègre'); box(ax,63,38,22,12,'resultat',label='ℤ/p est un corps')
arrow(ax,(25.5,44),(32.5,44),'varie',lw=1.8); arrow(ax,(55.5,44),(62.5,44),'fixe',lw=1.2)
text(ax,29,53.5,'Euclide','varie','s'); text(ax,59,53.5,'fini','fixe','s')
line(ax,[(29,43),(29,30.8)],'varie',dash=True)
box(ax,3,12,70,18,'varie',lw=1.8)
text(ax,38,25,'lemme d’Euclide','varie','m',weight='bold'); text(ax,38,17.5,r'$p\mid ab\Rightarrow p\mid a$ ou $p\mid b$','varie','m')
save(fig,'51-236')
