#include<stdio.h>
#include<math.h>

 struct account * search(struct account customer[],int n,int acc);
  struct account
   {char *name;
     int acc_no;
     float balance;
    };

main()
  { struct account *ptr,custemor[3]= {{"aashish",12,123}, {"aasha",123,145},{"ashu",45,1234.5}};
   int i=0,acc;

        for(i=0;i<3;i++)
         printf("%s %d %f \n",custemor[i].name,custemor[i].acc_no,custemor[i].balance);
         printf("enter account number=");
         scanf("%d",&acc);
     ptr=search(custemor,3,account);
     printf("%s %d %f \n",(*ptr).name,(*ptr).acc_no,(*ptr).balance);
  }


  struct account * search(struct account customer[],int n,int acc)
  { int i=0;
      for(i=0;i<3;i++)
        if(custemor[i].acc_no==acc)
        return &custemor[i];
      return nullptr;
  }
