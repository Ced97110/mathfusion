import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
# boîtes de 8 mm, pas de 9,5 mm : x = 6,75 + 9,5 i
xs=[6.75+9.5*i for i in range(8)]
for x in xs[:3]: box(ax,x,30,8,8,'sujet',label='7',size='m')
for x in xs[3:]: box(ax,x,30,8,8,'autre',label='7',size='m')
brace(ax,xs[0],xs[2]+8,39.5,'sujet',label=r'$7^{3}$',down=False,size='m')
brace(ax,xs[3],xs[7]+8,39.5,'autre',label=r'$7^{5}$',down=False,size='m')
brace(ax,xs[0],xs[7]+8,28.5,'resultat',label='3 + 5 = 8 facteurs : $7^{8}$',down=True,size='m')
text(ax,14,10,r'$7^{-2}$','limite','l')
box(ax,26,5,56,10,'limite',fill=False,label='−2 facteurs 7 : impossible',size='s',dash=True)
save(fig,'04-083')
