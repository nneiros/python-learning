#ερωτησεις και απαντησεις με σωστο,λαθος
import module1
import module2
#print(module1.question)
#print(module2.question)
sosto = 0
lathos = 0
t=int(input('Ποιο ειναι το τετραγωνο του 12? '))
print('Eδωσες απαντηση:',t)
if module2.answer is t:
    print('Σωστο')
    sosto = sosto+1
else:
    print('Λαθος')
    lathos = lathos+1
h=input('Ποια ειναι η πρωτευουσα του ν.Μαγνησιας? ')
d=[]
d.append(h)
print('Eδωσες απαντηση:',h)
#for h in d:
    #if h in module2.answer1:
if h == module2.answer1.lower():        
        print('Σωστο')
        sosto=sosto+1
else:
        print('Λαθος')
        lathos=lathos+1
#print(module1.answer)
#print(module2.answer)
f=input('Ποια ειναι η πρωτευουσα του ν.Αττικης? ')
d=[]
d.append(f)
print('Eδωσες απαντηση:',f)
#for f in d:
    #if f in module2.answer3:
if f == module2.answer3.lower():       
       print('Σωστο')
       sosto=sosto+1
else:    
       print('Λαθος')
       lathos=lathos+1
print('Βρηκες σωστα',sosto,'ερωτησεις και λαθος',lathos,\
      'ερωτησεις,επιτυχια=',sosto * 100 / (sosto+lathos),'%')#
if sosto<=2:
    print('Δεν τα πας καλα')
else:
    print('Εισαι φοβερος')
