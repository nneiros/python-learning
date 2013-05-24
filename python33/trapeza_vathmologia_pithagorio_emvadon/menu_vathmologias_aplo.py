
athroisma_vathmon=0
plhthos=0
fores=0






while fores<=5:
    print('--------Vathmoi Theologikou--------')
    print('-------1.Dose Vathmo---------------')
    print('-------2.Ektyposi synolikon arithmon mathimaton--------')
    print('-------3.Ektiposi mesou orou---------')
    print('-------4.Exit--------')
    epilogi=int(input('dialexe mia apo tis parapano epiloges'))
    fores=fores+1
    if epilogi==1:
      vathmo=int(  input('dose vathmo' ))
      plhthos=plhthos+1
      athroisma_vathmon=athroisma_vathmon+vathmo
    elif epilogi==2:
        print("o synolikos arithmos mathimaton ", plhthos )

    elif epilogi==3:
        mesos_oros= athroisma_vathmon/plhthos
        print("o mesos oros einai",mesos_oros)

    elif epilogi==4:
        print("exodos")
        break

    else:
        print("lathos epilogi")
        
    
        
