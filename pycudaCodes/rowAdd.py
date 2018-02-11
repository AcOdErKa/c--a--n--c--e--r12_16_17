import numpy as np
from pycuda import driver, compiler, gpuarray, tools
import pycuda.autoinit

kernel="""
__global__ void matrixAdd(int *a,int *r)
{
    int tx=threadIdx.x;
    int ty=threadIdx.y;

    int pvalue=0;

    for(int i=0 ; i< %(SIZE)s ;++i)
    {
        
        int ele=a[i];
        pvalue+=ele;
    }
    
    r[tx]=pvalue;
}
"""

SIZE=4
#r[ty * %(SIZE)s + tx]=pvalue; --Kernel

#a_cpu=np.random.randint(50,size=SIZE,size=SIZE)
a_cpu=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
#c_cpu=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
c_cpu=np.array([0,0,0,0])

a_gpu=gpuarray.to_gpu(a_cpu)
#c_gpu = gpuarray.empty((SIZE, SIZE), np.int32)
c_gpu=gpuarray.empty((SIZE), np.int32)
kernel=kernel %{
    'SIZE':SIZE
    }

mod=compiler.SourceModule(kernel)
results=mod.get_function("matrixAdd")

results(a_gpu,c_gpu,block=(SIZE,SIZE,1))
print "Original Matrix"
print a_gpu.get()

print "Sum of each rows"
print c_gpu.get()
