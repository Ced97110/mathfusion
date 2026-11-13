import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,8,38,'3','encre','xl')
line(ax,[(17,30),(13,30),(13,46),(17,46)],'autre',lw=1.4); line(ax,[(79,30),(83,30),(83,46),(79,46)],'autre',lw=1.4)
text(ax,28,38,r'$2+4$','encre','l'); box(ax,40,31,34,14,'sujet',label=r'$(1+1)$',size='l')
text(ax,24,18,'crochets','autre','m'); arrow(ax,(20,22),(14,28),'autre')
text(ax,58,18,'parenthèses','sujet','m'); arrow(ax,(57,22),(57,30),'sujet')
text(ax,44,5,r'$=30$','resultat','l')
save(fig,'12-048')
