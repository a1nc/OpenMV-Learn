#include<stdio.h>

int MyAtoI(unsigned char param)
{
	if(param>='a' && param<='f'){
		return (param-'a'+10);
	}else{
		return (param-'0');
	}
}


void DataAnalysis(unsigned char *buf,unsigned char buf_len)
{
	unsigned char pos=0;
	unsigned char flag=0;
	int cksum=0;
	int temp_ck=0;
	int pos_x=0;
	int pos_y=0;
	unsigned char _str[] = "aaaa0b02";//"";
	for(;pos<8;pos++){
		if(_str[pos]!=buf[pos]){
			flag=1;//bad packet
		}
	}
	
	if(flag==0){
		for(;pos<12;pos++){
			pos_x=pos_x*16+MyAtoI(buf[pos]);
			pos_y=pos_y*16+MyAtoI(buf[pos+4]);
		}
	}
	
	for(pos=0;pos<16;pos=pos+2){
		temp_ck = MyAtoI(buf[pos])*16+MyAtoI(buf[pos+1]);
		cksum = cksum+temp_ck;
	}

	temp_ck = 0;
	temp_ck = MyAtoI(buf[16])*16*16*16+MyAtoI(buf[17])*16*16;
	temp_ck = temp_ck + MyAtoI(buf[18])*16+MyAtoI(buf[19]);
	if(temp_ck == cksum){
		printf("temp_ck: %d\n",temp_ck);
		printf("cksum  : %d\n",cksum);
		printf("pos    : (%d,%d)\n",pos_x,pos_y);
	}
}

int main(){
	unsigned char test_str[]="aaaa0b02007d007d025b";
	unsigned char len = 20;
	DataAnalysis(test_str,len);
	getchar();
	getchar();
	return 0;
}
