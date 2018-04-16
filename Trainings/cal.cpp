#include <iostream>
using namespace std;

string compare(char s[]){
    char a[1000];
    char b[1000];
    int j=0;
    for (int i=0;s[i];i++){
        if (s[i]='+' || s[i]='-' || s[i]='*' || s[i]='/' || s[i]='**'){
            b[j] = s[i];
            j++;
        }
        else{
            b[j] = 'ID';
            j++;
        }
    }
    return b;
}
int main(){
    char s[1000];
    cout << "Please enter your string" << endl;
    cin >> s;
    char b[1000];
    b = compare(s);
    for (int i=0;b[i];i++){
        cout << b[i];
    }
    return 0;
}