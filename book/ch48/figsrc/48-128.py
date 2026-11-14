import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,66,'la formule, pas le numéro','encre','m',weight='bold')
R=[(46,'sujet','un noyau et une image',r'$G/\ker f\cong\mathrm{im}\,f$'),(28,'varie',r'$HN$ et $H\cap N$',r'$HN/N\cong H/(H\cap N)$'),(10,'autre','un quotient de quotient',r'$(G/N)/(H/N)\cong G/H$')]
for y,r,a,b in R:
    box(ax,3,y,34,14,r,label=a,size='s'); box(ax,40,y,46,14,r,label=b,size='s')
save(fig,'48-128')
