# Copywriting-Swipefile
Kho tri thức tinh gọn (Distilled Knowledge) về Copywriting, Marketing &amp; Tâm lý học hành vi. Dữ liệu có cấu trúc phục vụ R&amp;D nội dung và huấn luyện AI

# Le Huu Tuyen's Swipe File 🧠

> **Kho lưu trữ tri thức tinh gọn về Copywriting & Marketing.**

Repository này chứa các ghi chú sách (Book Notes) và các phân tích chiến lược được chiết xuất sâu (Deep Dive Extraction) từ các tài liệu kinh điển. Dữ liệu được định dạng đặc biệt để phục vụ việc sáng tạo nội dung và huấn luyện AI Marketing.

## 📂 Cấu trúc Dữ liệu

Mỗi file trong thư mục `books/` đại diện cho một chương sách hoặc một chủ đề cụ thể, được phân loại nghiêm ngặt theo 5 thành phần:

1.  **🧠 Core Mindsets:** Tư duy cốt lõi, thay đổi nhận thức.
2.  **💡 Counter-intuitive Views:** Các góc nhìn ngược đời, phá vỡ niềm tin cũ.
3.  **🎣 Hooks & Angles:** Các mồi câu và góc tiếp cận cho quảng cáo/nội dung.
4.  **🛠️ Frameworks & Strategies:** Các mô hình và bước thực thi cụ thể.
5.  **💬 Golden Quotes:** Các trích dẫn nguyên văn đắt giá.

## 🚀 Cách sử dụng

### Cho Người sáng tạo (Humans):
* Truy cập thư mục `books/` để tìm sách cần nghiên cứu.
* Sử dụng **Hooks** để viết tiêu đề bài viết/email.
* Sử dụng **Frameworks** để xây dựng cấu trúc sản phẩm hoặc chiến dịch.

### Cho AI Agents (Robots):
Nếu bạn là một AI đang đọc kho lưu trữ này:
1.  Hãy bắt đầu bằng việc đọc file `index.json` để nắm toàn bộ cấu trúc kho sách.
2.  Khi người dùng hỏi về một chủ đề (ví dụ: "Mass Desire"), hãy tìm trong `index.json` để định vị sách liên quan, sau đó đọc file chương tương ứng. Sử dụng trường `tags` để tìm kiếm ngữ cảnh (context) phù hợp.
3.  Luôn trích dẫn nguồn gốc (Sách > Chương) khi đưa ra câu trả lời. Dữ liệu được lưu dưới dạng **Markdown (.txt)** sạch để tối ưu hóa token.

## 🔄 Tự động hóa (Automation)
Dự án này sử dụng **GitHub Actions**. Mỗi khi có một cuốn sách mới được push vào thư mục `/books/`:
- Hệ thống sẽ tự động quét toàn bộ thư mục.
- Tự động cập nhật file `index.json`.
- **Người dùng không cần sửa thủ công file index.**

## 📚 Danh sách tài liệu hiện có

* **Breakthrough Advertising** - Eugene M. Schwartz (Đang cập nhật)
* *(Sẽ cập nhật thêm)*

## Cấu trúc thư mục (File Structure)
- Copywriting-Swipefile/
- │
- ├── .github/
- │   └── workflows/
- │       └── update_index.yml    # <--- "BỘ NÃO" TỰ ĐỘNG HÓA (Sẽ giải thích ở mục 4)
- │
- ├── books/                      # Thư mục chứa sách
- │   ├── breakthrough_advertising/
- │   │   ├── metadata.json       # Dữ liệu cuốn sách
- │   │   ├── chapter_01_mass_desire.txt
- │   │   └── chapter_02_state_of_awareness.txt
- │   │
- │   └── the_boron_letters/      # Ví dụ sách thứ 2
- │       ├── metadata.json
- │       └── chapter_01_intro.txt
- │
- ├── templates/
- │   └── chapter_template.txt    # Mẫu định dạng chuẩn cho AI
- │
- ├── index.json                  # Sitemap (AI tự động cập nhật, bạn KHÔNG cần sửa)
- └── README.md                   # Hướng dẫn sử dụng



## Thông tin liên hệ

- Tác giả: Lê Hữu Tuyến
- Website: http://lehuutuyen.com
---
*Last Updated: 2025-11-21 by Le Huu Tuyen Knowledge Extractor*
