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
