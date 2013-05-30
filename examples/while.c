


// int prueba(int x, int y){
// 	while(a<=10){
// 		x=x+y;
// 		a=n+1;
// 	}
// 	if(a==0);
// 	return x;

// }

int prueba(int x,int y){
	if(y==0){
		return 1;
	}
	else
		return y+prueba(x,y-1);
}



