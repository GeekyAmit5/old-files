#include<stdio.h>
int main()
{
    FILE *fp;
    int i,n,f,c,sum=0;
    printf("How many numbers you want to add?");
    scanf("%d",&n);
    fp=fopen("test.txt","w");
    printf("Enter the numbers : ");
    for(i=0;i<n;i++)
    {
        scanf("%d",&f);
        fprintf(fp,"%d\n",f);
    }
    fclose(fp);
    fp=fopen("test.txt","r");
    fscanf(fp,"%d",&c);
    while(c!=EOF)
    {
        sum+=c;
        fscanf(fp,"%d",&c);
    }
    fclose(fp);
    fp=fopen("test.txt","a");
    fprintf(fp,"%d",sum);
    fclose(fp);
    return 0;
}
