import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,3,56,50,13,'sujet',label=r'on suppose $1/3 = N/10^n$')
box(ax,3,32,50,13,'varie',label=r'donc 3 divise $10^n$')
box(ax,3,8,50,13,'limite',label=r'$10^n$ n’a que 2 et 5')
arrow(ax,(28,56),(28,45)); arrow(ax,(28,32),(28,21),'limite')
text(ax,70,70,'aucun multiple de 3','limite','s')
for i,(a,b) in enumerate((('10','10 = 3×3 + 1'),('100','100 = 3×33 + 1'),('1 000','1 000 = 3×333 + 1'))):
    box(ax,57,54-i*14,30,10,'limite',label=b,size='s')
text(ax,28,2.5,'impossible','limite','s')
save(fig,'08-087')
