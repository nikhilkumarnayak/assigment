# Problem-1
import numpy as np

# initializing lists
test_list = [[1,2,0,0,1,1,5,6,5]]
test_list_1 = [[1,2,0],[0,1,1],[5,6,5]]

# printing original list
# print("The original list : " + str(test_list))

text = np.array(test_list)
print("The original list : " + str(text))

reshape = text[0].reshape(3, 3)
print(reshape)

print(np.mean(reshape))
print(np.std(reshape))

zeroval= np.argwhere(reshape == 0)
print(zeroval)


shape = zeroval.shape
for i in shape:
    print(i)
    row, col = np.where(reshape == 0)
    print(row, col)
    val = reshape[row,col]
    print(val)
    reshape[col] = reshape[col].replace(0, val)

print(reshape)

