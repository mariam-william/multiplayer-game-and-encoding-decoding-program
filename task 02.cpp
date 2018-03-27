#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    string data;
    int Number_of_lines = 0;

    ifstream infile;
    infile.open("new1.txt");

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            getline(infile,data);
            cout << data << endl;
            Number_of_lines++;
        }
    cout << "Number of lines= " << Number_of_lines << " lines";
    }

    infile.close();



    return 0;
}
