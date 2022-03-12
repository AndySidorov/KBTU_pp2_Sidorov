import os
print(os.access(r"C:\Users\Chipchilinka\Desktop\Codes", os.F_OK))
print(os.access(r"C:\Users\Chipchilinka\Desktop\Codes", os.R_OK))
print(os.access(r"C:\Users\Chipchilinka\Desktop\Codes", os.W_OK))
print(os.access(r"C:\Users\Chipchilinka\Desktop\Codes", os.X_OK))