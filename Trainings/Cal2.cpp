#include<iostream>
#include<string>
#include<cctype>
using namespace std;
class token{
	string type;
	double value;
	public:
		token(string a,double b=0){
			type=a;
			value=b;
		}
		void print(void){
			cout<<type<<endl;
			cout<<value<<endl;
		}
};
char buf[100];
int index=0;

double T ();
double F ();

double E (void) {
	double x=T();
	while(buf[index]=='+'||buf[index]=='-'){
	int k=1;
	double y;
	if(buf[index]=='+'){
		token t("PLUS");
		t.print();
		k=0;
	}
	else if(buf[index]=='-'){
		token t("MINUS");
		t.print();
		k=1;
	}
	index++;
	y=T();
	if(k==0)
		x+=y;
	else
		x-=y;		
	}
return x;
}
	
	
double T(void){
	double x=F();
	while(buf[index]=='+'||buf[index]=='-'){
	int k=1;
	double y;
	if(buf[index]=='+'){
		token t("PLUS");
		t.print();
		k=0;
	}
	else if(buf[index]=='-'){
		token t("MINUS");
		t.print();
		k=1;
	}
	
	index++;
	y=F();
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
	token t("ID",y);
	t.print();	
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
