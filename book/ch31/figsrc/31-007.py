import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax,23,60,'fraction','sujet','s'); text(ax,67,60,'nom court','resultat','s')
rows=[('1/cos 30° ≈ 1,1547','sec 30°'),('1/sin 25° ≈ 2,3662','cosec 25°'),('cos 40°/sin 40° ≈ 1,1918','cotan 40°')]
for i,(a,b) in enumerate(rows):
    y=40-i*17
    box(ax,2,y,44,12,'sujet',label=a,size='s')
    box(ax,56,y,30,12,'resultat',label=b,size='m')
    arrow(ax,(46,y+6),(56,y+6),'varie')
text(ax,44,3,'mêmes valeurs, écriture plus courte','encre','s')
save(fig,'31-007')
