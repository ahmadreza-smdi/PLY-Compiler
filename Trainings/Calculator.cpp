#include <iostream>
using namespace std;

int index = 0;
char buf[1000];

void S(void){
    cout << "Please enter the string :"<<endl;
    cout << "Notice : Dont forget to put $ at the end!"<<endl;
    cin >> buf;
    cout << buf;
}

double E(void){
    double x = T();
}

int main(){
    S();
    return 0;
}