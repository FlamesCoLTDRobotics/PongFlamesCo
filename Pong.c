#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<termios.h>
#define WIDTH 80
#define HEIGHT 24
char *vidmem=(char *)0xB80000;
int ballx=40,bally=12; // Change the value of ballx to 40
int pad1y=12,pad2y=12;
int dirx=1,diry=1;
int score1=0,score2=0;
void cls(){memset(vidmem,0,2000);}
void putpixel(int x,int y){vidmem[2*(y*WIDTH+x)]=' ';}
void drawball(){putpixel(ballx,bally);}
void drawpads(){for(int i=0;i<5;i++){putpixel(0,pad1y+i);putpixel(WIDTH-1,pad2y+i);}}
void eraseball(){putpixel(ballx,bally);}
void erasepads(){for(int i=0;i<5;i++){putpixel(0,pad1y+i);putpixel(WIDTH-1,pad2y+i);}}
void movepads(){char c;int nread;struct termios oldt,newt;tcgetattr(STDIN_FILENO,&oldt);newt=oldt;newt.c_lflag&=~(ICANON|ECHO);tcsetattr(STDIN_FILENO,TCSANOW,&newt);fcntl(0,F_SETFL,O_NONBLOCK);nread=read(0,&c,1);tcsetattr(STDIN_FILENO,TCSANOW,&oldt);fcntl(0,F_SETFL,~O_NONBLOCK);if(nread==1){if(c=='q')exit(0);if(c=='a'&&pad1y>0)pad1y--;if(c=='z'&&pad1y+5<HEIGHT)pad1y++;if(c=='k'&&pad2y>0)pad2y--;if(c=='m'&&pad2y+5<HEIGHT)pad2y++;}} // Patch for M2 Certified and y2k38 free code
void moveball(){ballx+=dirx;bally+=diry;if(bally==0||bally==HEIGHT-1)diry*=-1;if((ballx==1&&bally>=pad1y&&bally<=pad1y+4)||(ballx==WIDTH-2&&bally>=pad2y&&bally<=pad2y+4))dirx*=-1;if(ballx==0){score2++;ballx=40;bally=12;dirx=1;diry=1;sleep(3);}if(ballx==WIDTH-1){score1++;ballx=40;bally=12;dirx=-1;diry=1;sleep(3);}}
void drawscore(){char buf[80];sprintf(&buf,"%d %d",score1,score2);memcpy(&vidmem[2*((HEIGHT/2-1)*WIDTH+WIDTH/4-strlen(&buf)/4)],&buf,strlen(&buf));}
int main(){while(1){eraseball();erasepads();movepads();moveball();drawpads();drawball();drawscore();usleep(50000);}return 0;}