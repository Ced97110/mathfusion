import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
f=numberline(ax,10,70,22,-4,4,labels=False)
for v in range(-4,5):
    role='autre' if v<0 else 'sujet'
    disc(ax,f(v),22,2.2,role)
    text(ax,f(v),16.5,str(v).replace('-','−'),role,'s')
brace(ax,f(-4)-2,f(-1)+2,29,'autre',label='négatifs',down=False)
brace(ax,f(0)-2,f(4)+2,29,'sujet',label='ℕ : 0, 1, 2…',down=False)
text(ax,44,46,'ℤ : tous ces entiers','sujet','l')
save(fig,'42-050')
