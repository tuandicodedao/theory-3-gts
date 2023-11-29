import math

def tinh_vi_tri_van_phao(R, H):
    # Bước 1: Tính thể tích của bể nước
    V_bể = math.pi * R**2 * H

    # Bước 2: Tính giá trị H_1/4 và H_7/8
    H_1_4 = 1/4 * H
    H_7_8 = 7/8 * H

    # Bước 3: Xác định vị trí cần đặt van phao
    h_van = (H_1_4 + H_7_8) / 2

    # Bước 4: Tính sai số của vị trí van phao
    sai_so_h_van = min(abs(H_7_8 - h_van), abs(H_1_4 - h_van))

    # Bước 5: Trả về kết quả
    return h_van, sai_so_h_van

# Ví dụ sử dụng:
R_bể = 65  # Bán kính đáy bể (đơn vị: mét)
H_bể = 65  # Chiều cao bể (đơn vị: mét)
h_van, sai_so_h_van = tinh_vi_tri_van_phao(R_bể, H_bể)

print("Vị trí cần đặt van phao: {:.2f} mét".format(h_van))
print("Sai số của vị trí van phao: {:.2f} mét".format(sai_so_h_van))
