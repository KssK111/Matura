# # funkcja SzukajIdola(A[][])
# # 	kandydat ← 0
# # 	jest_kandydat ← fałsz
# # 	dopóki kandydat<n oraz nie jest_kandydat wykonuj
# # 		j ← 0
# # 		A[kandydat][kandydat] ← prawda
# # 		dopóki j<n oraz A[j][kandydat] wykonuj
# # 			j ← j + 1
# # 		jeśli j = n to jest_kandydat ← prawda
# # 		w przeciwnym przypadku kandydat ← kandydat + 1
# # 	jeśli nie jest_kandydat to zwróć -1 i zakończ
# #
# # 	j ← 0
# # 	A[kandydat][kandydat] ← fałsz
# # 	dopóki j<n oraz nie A[kandydat][j] wykonuj j ← j + 1
# # 	jeśli j = n to zwróć kandydat i zakończ
# # 	w przeciwnym przypadku zwróć -1 i zakończ
#
# def SzukajIdola(A):
#     kandydat = 0
#     n = len(A)
#     jest_kandydat = False
#     while kandydat < n and not jest_kandydat:
#         j = 0
#         A[kandydat][kandydat] = True
#         while j < n and A[j][kandydat]:
#             j = j + 1
#         if j == n:
# 			jest_kandydat = True
# 		else:
# 			kandydat = kandydat + 1
#     if not jest_kandydat:
# 		return -1
# 	return kandydat