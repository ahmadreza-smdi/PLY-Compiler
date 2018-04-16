#include<iostream>
#include<string>
#include<cctype>
using namespace std;
char buf[100];
int index=0;

double T ();
double F ();

double E (void) {
	double x=T();
	cout<<x<<endl;
	while(buf[index]=='+'||buf[index]=='-'){
	int k=1;
	double y;
	if(buf[index]=='+'){
		k=0;
	}
	index++;
	y=T();
	cout<<y<<endl;
	if(k==0)
		x+=y;
	else
		x-=y;		
	}
return x;
}
	
	
double T(void){
	double x=F();
	cout<<x<<endl;
	while(buf[index]=='+'||buf[index]=='-'){
	int k=1;
	double y;
	if(buf[index]=='+'){
		k=0;
	}
	index++;
	y=F();
	cout<<y<<endl;
	if(k==0)
		x+=y;
	else
		x-=y;		
	}
return x;	
}


double F(void){
	if(buf[index]=='('){
		index++;
		int u=E();
		if(buf[index]!=')'){
			cout<<"erro"<<endl;
			
		}
		else{
			index++;
			return u;
		} 
	}
	else if(isdigit(buf[index])){
		string z;
		while(isdigit(buf[index])){
			z+=buf[index];
		index++;
		}
	int y = stoi(z);	
	return y;	
	}
	else{
		cout<<"error";
	}
}	

int main(){
	cout<<"Please enter your own phrase:";
	cin>>buf;
	cout<<"result:"<<E()<<endl;
return 0;
}
