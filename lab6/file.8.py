from base64 import b32decode
import os
b1 = os.path.exists(r"C:\Users\Chipchilinka\Desktop\Codes\lab6\delete.txt")
b2 = os.access(r"C:\Users\Chipchilinka\Desktop\Codes\lab6\delete.txt", os.F_OK)
b3 = os.access(r"C:\Users\Chipchilinka\Desktop\Codes\lab6\delete.txt", os.R_OK)
b4 = os.access(r"C:\Users\Chipchilinka\Desktop\Codes\lab6\delete.txt", os.W_OK)
b5 = os.access(r"C:\Users\Chipchilinka\Desktop\Codes\lab6\delete.txt", os.X_OK)
if b1 and b2 and b3 and b4 and b5:
    os.remove(r"C:\Users\Chipchilinka\Desktop\Codes\lab6\delete.txt")