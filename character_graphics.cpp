//Saurav Hossain
//10/30/18
//Shit

#include <iostream>
using namespace std;

int main() 
{
  int x;
  cin >> x; 
  for(int i = 0; i < x; i++)
  {
    cout << "\n";
    for(int j = 0; j <= i; j++)
      cout << "*";
  }
}