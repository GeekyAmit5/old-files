#include<stdio.h>
#include<stdlib.h>
int max(int *,int);
int main()
{
    int n,*a,i,(*p)(int *,int);
    p=&max;
    printf("Enter the value of n : ");
    scanf("%d",&n);
    a=calloc(n,sizeof(int));                        /*  a=malloc(n*sizeof(int));  this can also be used */
    printf("\nEnter the elements : \n");
    for(i=0;i<n;i++)
    {
        scanf("%d",(a+i));
    }
    printf("The maximum is : %d",p(a,n));
    return 0;
}
int max(int *a,int n)
{
    int m=a[0],i;
    for(i=0;i<n;i++)
        if(m<a[i])
            m=a[i];
    return m;
}
