import streamlit as st

st.title("Đăng ký lịch cắt điện tuần")

don_vi = st.text_input("Tên đơn vị đăng ký")
ten_duong_day = st.text_input("Tên đường dây/TBA")
ngay_bat_dau = st.date_input("Ngày giờ bắt đầu cắt điện")
ngay_ket_thuc = st.date_input("Ngày giờ kết thúc cắt điện")
noi_dung = st.text_area("Nội dung công việc")
phuong_an = st.text_area("Phương án chuyển tải")
slkh = st.number_input("Số lượng khách hàng ảnh hưởng", min_value=0)
saidi = st.number_input("SAIDI dự kiến (phút)", min_value=0.0)

if st.button("Gửi đăng ký"):
    st.success("Đăng ký thành công!")
    import pandas as pd
import os

# Dữ liệu mới
new_data = {
    "Đơn vị": [don_vi],
    "Đường dây/TBA": [ten_duong_day],
    "Ngày bắt đầu": [ngay_bat_dau],
    "Ngày kết thúc": [ngay_ket_thuc],
    "Nội dung": [noi_dung],
    "Phương án chuyển tải": [phuong_an],
    "SLKH": [slkh],
    "SAIDI": [saidi],
    "Ghi chú": [ghi_chu]
}

new_df = pd.DataFrame(new_data)

# Kiểm tra file đã tồn tại chưa
file_path = "lich_cat_dien.xlsx"

if os.path.exists(file_path):
    # Nếu có file rồi thì append dữ liệu mới
    existing_df = pd.read_excel(file_path)
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
else:
    # Nếu chưa có file thì tạo file mới
    updated_df = new_df

# Ghi đè lại file
updated_df.to_excel(file_path, index=False)

