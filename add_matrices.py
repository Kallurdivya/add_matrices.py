A = [[0,0,0],[0 ,0,0],[0 ,0,0]] 
for i in range(0,3):
  for j in range(0,3):
    value=int(input("Enter A matrix :")) 
    A[i][j]=value 
print("A Matrix is ") 
for r in A:
  print(r) 
B = [[0,0,0],[0 ,0,0],[0 ,0,0]] 
for i in range(0,3):
  for j in range(0,3):
    value=int(input("Enter B matrix :"))
    B[i][j]=value 
print("\nB Matrix is ")
for r in B:
  print(r) 
result = [[0,0,0],[0,0,0],[0,0,0]] 
for i in range(len(A)):
  for j in range(len(A[0])):
    result[i][j] = A[i][j] + B[i][j] 
print("\nResults Matrix is ")
for r in result: 
  print(r) 