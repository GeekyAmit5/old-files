#include<stdio.h>
#include<string.h>

int main()
{
    char c[20],pwd[20]="abc";
    int cnt=0,i;
    label:
        printf("Enter the password : ");
        for(i=0;(c=getchar())!='\n';i++)
        scanf("%c",c[i]);
        if(!strcmp(pwd,c))
        printf("Login Successful !");
        else
        {
            cnt++;
            if(cnt==3)
            {
                printf("Login has Blocked try again after sometime!");
            }
            printf("Password did not match!");
            if(cnt!=3)
            goto label;
        }
    return 0;
}
