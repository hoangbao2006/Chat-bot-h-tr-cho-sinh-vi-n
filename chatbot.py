# Chatbot tư vấn sinh viên - phiên bản cơ bản
import re

# Danh sách kịch bản (intent và response)
faq = {
    r"(đăng ký tín chỉ|đăng ký môn học)": "Đăng ký tín chỉ bắt đầu từ tuần 2 mỗi học kỳ, qua cổng sinh viên.",
    r"(học phí|nộp học phí)": "Học phí trung bình là 350.000đ/tín chỉ. Bạn có thể nộp online qua ngân hàng.",
    r"(lịch học|thời khóa biểu)": "Lịch học được cập nhật trên hệ thống LMS mỗi tuần.",
    r"(liên hệ|phòng đào tạo|giáo vụ)": "Bạn có thể liên hệ Phòng Đào tạo tại tầng 2 nhà A1, hoặc gọi 0123-456-789.",
    r"(thi cuối kỳ|lịch thi)": "Lịch thi cuối kỳ sẽ được công bố sau tuần thứ 10 trên website trường.",
    r"(xin nghỉ học|bảo lưu)": "Để bảo lưu, bạn cần làm đơn và nộp tại Phòng Công tác sinh viên."
}

def chatbot_reply(user_input):
    # Duyệt qua các pattern trong faq
    for pattern, response in faq.items():
        if re.search(pattern, user_input.lower()):
            return response
    return "Xin lỗi, mình chưa hiểu câu hỏi này. Bạn có thể liên hệ phòng đào tạo để được hỗ trợ thêm."

# Demo chatbot
print("🤖 Chatbot: Xin chào! Tôi là trợ lý ảo hỗ trợ sinh viên.")
while True:
    user_input = input("👩‍🎓 Bạn: ")
    if user_input.lower() in ["thoát", "exit", "quit"]:
        print("🤖 Chatbot: Cảm ơn bạn! Chúc bạn học tập tốt!")
        break
    print("🤖 Chatbot:", chatbot_reply(user_input))
