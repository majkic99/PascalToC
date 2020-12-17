int  pow_rek(int a, int b);
int main(){
int a;
int b;
scanf("%d",&a);
scanf("%d",&b);
printf("%d",pow_rek(a, b));
printf("\n");
}
int  pow_rek(int a, int b){
if (b == 0){
return(1);
}
return(a*pow_rek(a, b-1));
}