// FCI – Programming 1 – 2018 - Assignment 2
// Program Name: ROT13.cpp
// Last Modification Date: 27/02/2018
// Author1 and ID and Group: Mariam Makram William 20170283 G_11;
// Teaching Assistant: Eng. Khadiga Khaled Eng. Dina Mohamed.
// Purpose: Ciphering and Deciphering messages.

#include <iostream>
#include <string>

using namespace std;

int main()

{
    //Ciphering the message.

    string c;
    cout << "                                   ROT13 Cypher" << endl;

    int x;
    cout << "Ahlan ya user ya habibi.\nWhat do you like to do today? \n";
    cout <<  "\n Press: \n  1- to Cipher a message. \n  2- to Decipher a message. \n  any key to exit. " << endl;
    cout << "Number: ";
    cin >> x;

    if (x==1)
    {
        cout << endl << "Enter the message to be Ciphered: ";
        cin.ignore();
        getline(cin,c);

        cout << endl << "ROT13: ";
        for ( int i=0 ; i<=c.length() ; i++)
            {
            if ( (c [i] >= 'a' && c [i] < 'n') || (c [i] >= 'A' && c [i] < 'N'))
            {
                c[i]+=13;
            }
            else if ( (c [i] >= 'n' && c [i] <= 'z' ) || (c [i] >= 'N' && c [i] <= 'Z'))
                {
                    c[i]-=13;
                }
            }
        cout << c << endl;
        }

    //Deciphering the message.
    else if (x==2)
    {
        cout << endl << "Enter the message to be Deciphered: ";
        cin.ignore();
        getline(cin,c);

        cout << endl << "ROT13: ";
        for ( int i=0 ; i<=c.length() ; i++)
            {
            if ( (c [i] >= 'a' && c [i] < 'n') || (c [i] >= 'A' && c [i] < 'N'))
            {
                c[i]+=13;
            }
            else if ( (c [i] >= 'n' && c [i] <= 'z' ) || (c [i] >= 'N' && c [i] <= 'Z'))
                {
                    c[i]-=13;
                }

            }
      cout << c << endl;
      }
    else

    return 0;
}
