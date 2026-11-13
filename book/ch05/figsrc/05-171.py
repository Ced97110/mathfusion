import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,44,74,r'$2^{2^{n}}+1$','sujet','xl')
text(ax,44,66,'l’exposant double à chaque pas','varie','s')
for n in range(5):
    e=2**n; y=54-n*9
    text(ax,2,y,r'$n=%d$'%n,'encre','s',ha='left')
    box(ax,16,y-2,e*2.4,4,'varie',r=0.3,lw=0.6)
    val=2**e+1
    s=f'{val:,}'.replace(',','\\,')
    text(ax,56,y,r'$2^{%d}+1=%s$'%(e,s),'resultat','s',ha='left')
save(fig,'05-171')
