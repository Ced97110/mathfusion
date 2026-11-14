import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
text(ax,44,76,r'même partie en lettres : $x$','sujet','m')
for k,(n,y) in enumerate([(8,64),(5,52)]):
    for i in range(n): box(ax,14+7.5*i,y,6.5,8,'sujet',label=(r'$x$' if i==0 else None),size='s')
    text(ax,4,y+4,r'$%dx$'%n,'sujet','m',ha='left')
text(ax,44,42,r'même partie en lettres : $a^3$','autre','m')
cubes(ax,[(i,0,0) for i in range(4)],(16,26),3.2,'autre'); text(ax,4,30,r'$4a^3$','autre','m',ha='left')
cubes(ax,[(i,0,0) for i in range(8)],(16,6),3.2,'autre'); text(ax,4,10,r'$8a^3$','autre','m',ha='left')
text(ax,66,14,r'1 cube $=a^3$','autre','s')
save(fig,'15-042')
