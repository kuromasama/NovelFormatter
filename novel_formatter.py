import re
import os

def format_novel(input_file):
    """
    讀取小說文件並整理格式
    - 章節標題加上 # 符號
    - 統一段落格式和空行
    - 輸出為 txt 檔案
    """
    # 生成輸出檔案名稱，保持 .txt 副檔名
    output_file = 'adjusted_' + input_file
    
    try:
        # 檢查輸入檔案是否存在
        if not os.path.exists(input_file):
            print(f"錯誤：找不到檔案 '{input_file}'")
            return
        
        # 讀取檔案
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 章節標題的正則表達式
        #chapter_pattern = r"^\s*(簡介|內容簡介|序|推薦序|楔子|尾聲|後記|番外|[第卷][0123456789一二三四五六七八九十零〇百千兩]*[卷回部章節])\s*([^課].*|)$"
        chapter_pattern = r"^\s*(簡介|简介|內容簡介|内容简介|序|推薦序|推荐序|楔子|尾聲|尾声|後記|后记|番外|[第卷][0123456789一二三四五六七八九十零〇百千兩两]*[卷回部章節])\s*([^(課|课)].*|)$"
        # 將內容按章節分割
        chapters = []
        current_chapter = []
        lines = content.split('\n')
        
        for line in lines:
            # 如果是新的章節標題
            if re.match(chapter_pattern, line, re.I):
                if current_chapter:
                    chapters.append('\n'.join(current_chapter))
                # 將章節標題加上 # 符號
                current_chapter = [f"# {line.strip()}"]
            else:
                # 處理段落文字
                cleaned_line = line.strip()
                if cleaned_line:
                    current_chapter.append(cleaned_line)
        
        # 加入最後一章
        if current_chapter:
            chapters.append('\n'.join(current_chapter))
        
        # 格式化每個章節
        formatted_chapters = []
        for chapter in chapters:
            # 分割章節標題和內容
            chapter_lines = chapter.split('\n')
            title = chapter_lines[0]  # 現在標題已經包含 #
            
            # 處理章節內容
            content_lines = chapter_lines[1:]
            formatted_content = []
            
            # 確保段落之間有適當的空行
            for line in content_lines:
                if line.strip():
                    formatted_content.extend(['', '    ' + line.strip()])
            
            # 組合章節
            formatted_chapter = title + '\n' + '\n'.join(formatted_content)
            formatted_chapters.append(formatted_chapter)
        
        # 寫入新檔案
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(formatted_chapters))
        
        print(f"格式化完成！新檔案已儲存為：{output_file}")
        
    except Exception as e:
        print(f"處理檔案時發生錯誤：{str(e)}")

def main():
    print("小說格式整理工具")
    print("===============")
    print("此工具會：")
    print("1. 在章節標題前加上 # 符號")
    print("2. 統一段落格式和空行")
    print("3. 產生格式化後的 txt 檔案\n")
    
    while True:
        # 讓使用者輸入檔案名稱
        filename = input("請輸入小說檔案名稱（包含.txt）或輸入'q'退出：")
        
        if filename.lower() == 'q':
            print("程式結束")
            break
            
        if not filename.endswith('.txt'):
            print("錯誤：檔案必須是 .txt 格式")
            continue
            
        format_novel(filename)
        
        # 詢問是否繼續處理其他檔案
        cont = input("\n是否要處理其他檔案？(y/n)：")
        if cont.lower() != 'y':
            print("程式結束")
            break

if __name__ == '__main__':
    main()
    print("\n按 Enter 鍵結束...")
    input()