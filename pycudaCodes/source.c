#include<stdlib.h>
__global__ void pos(int *arr,int *len,int *l,int *pos)
{
    int tx=threadIdx.x;
    int i,j,ctr=0,jmp=0;    //ctr=> counter for pos, jmp=> no of elements required to get to next arr row
    int len_shift=0;        //no of elements required to get to current len
    int pos_shift=tx*pos_size;  //no of elements required to get to current pos
    
    for(i=0;i<tx;i++)
        len_shift+=l[i];        //adding previous l[i]<l[tx] to get to current location
    
    for(i=0;i<l[tx];i++)
    {
        for(j=0;j<len[len_shift+i];j++)
        {
            if(arr[tx+jmp+j])
                pos[pos_shift + (count++)]=1;
        }
        jmp+=len[tx+i];
    }
}

pos_size=10 //size of each list in pos(number of elements in universe)