#include <iostream>

using namespace std;

int main()
{
    int x=3,y=1,z=8;

    cout << "Before swap: n1= " << x << " n2= " << y << " n3=" << z << endl;

int n1, n2, n3;
    if (x>y && x>z)
    {
        n1=x;
        if (y>z)
        {
            n2=y;
            n3=z;
        }
        else
        {
            n2=z;
            n3=y;
        }
    }

    else if (y>z && y>x)
    {
        n1=y;
        if (x>z)
        {
            n2=x;
            n3=z;
        }
        else
        {
            n2=z;
            n3=x;
        }
    }
    else
    {
        n1=z;
        if (x>y)
        {
            n2=x;
            n3=y;
        }
        else
        {
            n2=y;
            n3=x;
        }
    }
    cout << "After swap: n1= " << n1 << " n2= " << n2 << " n3=" << n3 << endl;


    return 0;
}
