#include <iostream>

using namespace std;

int gcd(int x,int y)
{
    if (x%y == 0)
    {
    	return y;
    }
    else
    {
    	return gcd(y,x%y);
    }
}

int main()
{
    int x,y;
    cout << "Enter the numbers : " << endl ;
    cin >> x>>y ;
    cout << "GCD of " << x <<" and "<<y<<" is : "<<gcd(x,y)<< endl;
    return 0;
}

