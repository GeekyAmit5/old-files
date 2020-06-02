#include<stdio.h>
float IP(float x[],float y[],int n)
{
    float s=0;
    for(int i=0;i<n;i++)
        s+=x[i]*y[i];
    return s;
}
float * BA(float x[],float y[],int n)
{
    float z[n];
    int i;
    for(i=0;i<n;i++)
        z[i]=(IP(y,x,n)/IP(x,x,n));
    return z;
}
int main()
{
    int i,n;
    printf("Enter the dimension : ");
    scanf("%d",&n);
    int x[n],y[n];
    printf("Enter v : ");
    for(i=0;i<n;i++)
        scanf("%f",&x[i]);
    printf("Enter w : ");
    for(i=0;i<n;i++)
        scanf("%f",&y[i]);
    printf("Best Approximation is : \n(");
    for(i=0;i<n;i++)
        printf("%f,",BA(x,y,n)[i]);
    printf(")\n");
    return 0;
}
