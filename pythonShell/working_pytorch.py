import torch

batch1=torch.randn(10,3)
print(batch1)
batch2=torch.randn(10,4)
print(batch2)
res=torch.bmm(batch1,batch2)

print(res.size())
