import scipy.linalg as ln
import numpy as np

# Đọc ma trận từ file input.txt
A = np.loadtxt("input.txt")

m, n = A.shape
n_diag = min(m, n)

U, S_diag, V = ln.svd(A)

# Tạo ma trận đường chéo S
S = np.zeros((n_diag, n_diag))
np.fill_diagonal(S, S_diag)
if m > n:
    S = np.concatenate((S, np.zeros((1, n))), axis=0)
elif m < n:
    S = np.concatenate((S, np.zeros((m, 1))), axis=1)

print('Ma tran A: \n%s \n' % A)
print('Ma tran truc giao U: \n%s \n' % U)
print('Check Frobenius U^TU-I: \n%s \n' % ln.norm(np.dot(U.T, U) - np.eye(m, m), 'fro'))
print('Ma tran truc giao V^T: \n%s \n' % V)
print('Check Frobenius V^TV-I: \n%s \n' % ln.norm(np.dot(V.T, V) - np.eye(n, n), 'fro'))
print('Ma tran duong cheo S: \n%s \n' % S_diag)
print('Ma tran S: \n%s \n' % S)
print('Check Frobenius U.S.V - A: \n%s \n' % ln.norm(np.dot(U, S.dot(V)) - A, 'fro'))
