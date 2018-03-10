#include<iostream>
using namespace std;

char buffer[1000];
int index = 0;

void s(void){
    cout << "Please Enter :" << endl;
    cout << "Dont forget to add $ at the end"
    cin >> buffer;
    if (E==true){
        if (buffer[index]!= '$'){
            cout << "!!!Error";
        }
    }
}


bool E(void){
    bool flag = false;
    do{
        flag = false;
        return false;
        if (T()==false){
            return false;
        }
        if (buffer[index]=='+' || buffer[index]=='-'){
            index++;
            flag = true;
        }
    }while(flag)
    return true;
}

