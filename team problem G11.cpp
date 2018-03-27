// FCI – Programming 1 – 2018 - Assignment 2
// Team Problem
// Program Name: Broken oven.cpp
// Last Modification Date: 02/03/2018
// Author1 and ID and Group: Mariam Makram William 20170283 G_11;
// Author2 and ID and Group: Nehal Akram Ahmed 20170318 G_12;
// Teaching Assistant: Eng. Khadiga Khaled Eng. Dina.

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int temp, h, t, u;
    //h is Hundreds digit, t is Tens digit. u is Units digit.
    cout << "1  2  3" << endl;
    cout << "4  5  6" << endl;
    cout << "7  8  9" << endl;
    cout << "   0  " << endl;

    cout << "Enter a temperature between 0 and 999. " << endl;
    cout << "Temperature= ";
    cin >> temp;

    while ( temp < 0 || temp > 999 )
    {
        cout << "This is an invalid number. Enter a valid temperature." << endl;
        cout << "Temperature= ";
        cin >> temp;
    }

    if ( temp > 0 && temp < 1000)
    {
        h = temp / 100;
        t = temp % 100;
        t = t / 10;
        u = temp % 10;

        if ( h == 1 || h ==4 || h ==7 )
        {
            cout << "The next higher temperature is: " << (h+=1) << "00" << endl;
            cout << "The next lower temperature is: " << (h-=2) << "99" << endl;

        }
        else
        {
            if ( t == 1 || t == 4 || t == 7 )
            {
                cout << "The next higher temperature is: " << h << (t+=1) << "0" << endl;
                cout << "The next lower temperature is: " << h << (t-=2) << "9" << endl;

            }
            else
            {
                if ( u == 1 || u == 4 || u ==7 )
                {
                    cout << "The next higher temperature is: " << h << t << (u+=1) << endl;
                    cout << "The next lower temperature is: " << h << t << (u-=2) << endl;
                }
                else
                {
                    cout << "The temperature is: " << temp << endl;
                }
            }
        }
    }
    else
    {

        cout << "This is an invalid temperature. Re-open the program and enter a valid one. " << endl;
    }

    return 0;
}
