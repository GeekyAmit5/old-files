#include<stdio.h>
#include<string.h>
struct account
{
	char *id;
	char *pwd;
     	int accno;
     	float bal;
};
main()
{
	struct account customer[3]= {{"amit","abc",123,1230.91}, {"ritesh","efg",456,19045.32},{"sajid","xyz",789,10234.57}};
   	int i=0,t=0,cnt=0;
	char *p,*uid;
	login:
	printf("Enter the UserID :");
	gets(uid);
	for(i=0;i<3;i++)
		if(!strcmp(uid,customer[i].id))
		{
			t=1;
			break;
		}
	if(t)
	{
		if(pwdCheck(customer[i]))
		{
			char r;
			printf("Login Succesful!\n");
			printf("Account Details Are :\n");
			printf("NAME = %s\nAccount No.= %d\nBalance = %.2f\n",customer[i].id,customer[i].accno,customer[i].bal);
			printf("Do you want to transfer amount?(y/n)\n");
			scanf("%c",&r);
			if(r=='y')
			{
				int acc,t=0,j;
				transfer :
				printf("Enter the account no.:");
				scanf("%d",&acc);
				for(j=0;j<3;j++)
					if(acc==customer[j].accno)
					{
						printf("NAME = %s\n",customer[j].id);
						t=1;
						break;
					}
				if(t)
				{
					float a;
					money:
					printf("Enter the amount :");
					scanf("%f",&a);
					if(a<=customer[i].bal)
					{
						customer[i].bal-=a;
						customer[j].bal+=a;
						printf("Transaction successful!\n");
						printf("Transaction Details are :\n");
					printf("transaction ID = 20192710\nAmount Transfered = %.2f\nBalance Left = %.2f\n",a,customer[i].bal);
					}
					else
					{
						printf("Insufficient balance!\n");
						printf("Your Balance is : %f\n",customer[i].bal);
						goto money;
					}
				}
				else
                {
					printf("Account no. is invalid\n");
					goto transfer;
                }
			}
			else
                printf("Logging Out!\n");
		}
		else
			printf("Login blocked!\n");
	}
	else
    {
		printf("Please Enter a Valid UserID\n");
		goto login;
    }
}
int pwdCheck(struct account customer)
{
	char *p;
	int t=0,cnt=0;
	attempt:
		printf("Enter the Password :");
		gets(p);
		if(!strcmp(p,customer.pwd))
			t=1;
		else
		{
			printf("Password is incorrect!\n");
			cnt++;
			if(cnt!=3)
			{
				printf("%d attempts left\n",3-cnt);
				goto attempt;
			}
		}
	return t;
}
