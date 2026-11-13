import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
ex=[r'$a\vee a$',r'$(a\vee a)\wedge I$',r'$(a\vee a)\wedge(a\vee a^{\prime})$',r'$a\vee(a\wedge a^{\prime})$',r'$a\vee O$',r'$a$']
tg=['par A4','par A5','par A3','par A5','par A4']
for i,e in enumerate(ex):
    y=76-i*15
    role='sujet' if i==0 else ('resultat' if i==5 else 'fixe')
    box(ax,4,y,58,9,role,label=e)
    if i<5:
        arrow(ax,(33,y),(33,y-6),'varie'); text(ax,38,y-3,tg[i],'varie','s',ha='left')
save(fig,'80-152')
