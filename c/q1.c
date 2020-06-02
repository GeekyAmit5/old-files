#include<stdio.h>
float norm (float []);
int main()
{
	float x[3];
	int i;
	printf("Enter the vector x :\n");
	for(i=0;i<3;i++)
	scanf("%f",&x[i]);
	printf("Norm = %f",norm(x));
	printf("\n");
	return 0;
}
float norm(float x[])
{
	int i;
	float *p,n=0;
	p=x;
	for(i=0;i<3;i++)
	{
		n+=*(p+i) * *(p+i) ;
	}
	return n;
}
