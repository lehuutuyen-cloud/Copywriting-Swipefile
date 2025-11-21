import os
import json
from datetime import datetime

# Cấu hình đường dẫn
BOOKS_DIR = 'books'
INDEX_FILE = 'index.json'

def generate_sitemap():
    library = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_books": 0,
        "books": []
    }

    # Kiểm tra nếu thư mục books tồn tại
    if not os.path.exists(BOOKS_DIR):
        print(f"Directory {BOOKS_DIR} not found.")
        return

    # Quét từng thư mục con trong /books/
    # sorted() giúp danh sách ổn định, không bị nhảy thứ tự mỗi lần chạy
    for book_folder in sorted(os.listdir(BOOKS_DIR)):
        book_path = os.path.join(BOOKS_DIR, book_folder)
        
        # Chỉ xử lý nếu là thư mục
        if os.path.isdir(book_path):
            book_data = {
                "id": book_folder,
                "info": {},
                "chapters": []
            }

            # 1. Đọc file metadata.json nếu có
            meta_path = os.path.join(book_path, 'metadata.json')
            if os.path.exists(meta_path):
                try:
                    with open(meta_path, 'r', encoding='utf-8') as f:
                        book_data["info"] = json.load(f)
                except Exception as e:
                    print(f"Error reading metadata for {book_folder}: {e}")
            else:
                # Nếu không có metadata, tạo info mặc định từ tên thư mục
                book_data["info"] = {
                    "title": book_folder.replace('_', ' ').title(),
                    "id": book_folder
                }
            
            # 2. Quét các file nội dung (.txt hoặc .md)
            # Loại bỏ metadata.json và các file ẩn
            valid_extensions = ('.txt', '.md')
            
            for file in sorted(os.listdir(book_path)):
                if file.endswith(valid_extensions) and file != 'metadata.json':
                    book_data["chapters"].append({
                        "filename": file,
                        "path": f"{BOOKS_DIR}/{book_folder}/{file}"
                    })
            
            # Chỉ thêm vào danh sách nếu thư mục có chứa chương hoặc metadata
            if book_data["chapters"] or book_data["info"]:
                library["books"].append(book_data)

    library["total_books"] = len(library["books"])

    # Ghi ra file index.json
    try:
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump(library, f, indent=2, ensure_ascii=False)
        print(f"Sitemap ({INDEX_FILE}) updated successfully with {library['total_books']} items.")
    except Exception as e:
        print(f"Error writing index file: {e}")

if __name__ == "__main__":
    generate_sitemap()
