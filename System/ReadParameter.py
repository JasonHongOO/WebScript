import os
from win32com.client import Dispatch


def read_name():
    name_list = []
    with open("./NameList.txt" , mode = 'r',encoding="utf-8") as read_text: 
        for line in read_text:
            name_list.append(line.strip())

    return name_list

def readURL():
    web_list = []
    #開檔，讀出檔案路徑
    with open("./URL.txt" , mode = 'r',encoding="utf-8") as read_text: 
        for line in read_text:
            line=line.strip('\n')   #去除換行
            line=line.strip('')   #去除開頭、結尾的空白
            web_list.append(line)

    return web_list 
            
def read_profile(browser_num,window_select_profile_mode,multi_profile_mode):
    def window_select_profile():
        import tkinter as tk
        from tkinter import filedialog

        profile_name_list = []   #現在這邊還是 file name
        file_address = []
        final_select_address = []   #現在這邊是每個 file name 對應的 address

        def add_to_web_list():
            selected_files = files_listbox.curselection()
            for i in selected_files:
                profile_name_list.append(files_listbox.get(i))
                final_select_address.append(file_address[i])
            root.destroy()  #關閉視窗

        def select_all():
            files_listbox.select_set(0, tk.END)

        def select_clear():
            files_listbox.select_clear(0, tk.END)

        def browse_folder_path():
            folder_path = filedialog.askdirectory()
            folder_path_entry.delete(0, tk.END)
            folder_path_entry.insert(tk.END, folder_path)

            #list_files
            folder_path = folder_path_entry.get()
            if os.path.exists(folder_path):
                files = []
                file_address.clear() #每次重選資料夾時，先清空
                for root, _, filenames in os.walk(folder_path):
                    for filename in filenames:
                        file_address.append(os.path.join(root,filename))
                        files.append(filename)
                files_listbox.delete(0, tk.END)
                for f in files:
                    files_listbox.insert(tk.END, f)

        # 建立主視窗
        root = tk.Tk()
        root.title("List files in folder")
        row_offest = 40
        # 建立使用者輸入資料夾路徑的欄位
        folder_path_label = tk.Label(root, text="Folder path:")
        folder_path_label.grid(row=0,column=row_offest)
        folder_path_entry = tk.Entry(root, width=50)
        folder_path_entry.grid(row=0,column=row_offest+1)
        browse_button = tk.Button(root, text="Browse", command=browse_folder_path)
        browse_button.grid(row=0,column=row_offest+2)

        # 建立列出檔案的清單
        files_listbox = tk.Listbox(root, width=100, selectmode=tk.EXTENDED)
        files_listbox.grid(row=1,column=0,columnspan=250)

        # 建立按鈕，當使用者按下時選取所有檔案
        select_all_button = tk.Button(root, text="Select All", command=select_all)
        select_all_button.grid(row=0,column=row_offest+3)

        select_Clear_button = tk.Button(root, text="Select Clear", command=select_clear)
        select_Clear_button.grid(row=0,column=row_offest+4)

        # 建立按鈕，當使用者按下時將選取的檔案名稱加入 web_list 中
        add_to_web_list_button = tk.Button(root, text="Add to Web List", command=add_to_web_list)
        add_to_web_list_button.grid(row=6,column=0,columnspan=100)

        # 啟動主視窗
        root.mainloop()
        return profile_name_list,final_select_address

    def read_profile_file():
        #開檔，讀出檔案路徑
        with open("./Profile.txt" , mode = 'r') as read_text: 
            para_list = []
            for line in read_text:
                line=line.strip('\n')   #去除換行
                line=line.strip('')   #去除開頭、結尾的空白
                line = line.replace("\"","")
                line_ele = line.split(' ',2)
                para_list.append(line_ele[2])

            name_list = [i.split('=',1)[1] for i in para_list]

            return name_list, para_list
    #=======================================================================================#
    if window_select_profile_mode == 1 :
        files_name = []
        files_address = []
        files_name,files_address = window_select_profile()

        #總共有幾筆資料     (基本上讀取資料，網站的數量有多少就會直接被決定，使用者的設定是沒有意義的)
        if(multi_profile_mode == 1):
            browser_num = len(files_name)

        shell = Dispatch("WScript.Shell")
        for file in files_name:
            # print(file)
            shortcut = shell.CreateShortCut(files_address[files_name.index(file)])
            Targetpath = shortcut.Targetpath
            arguments = shortcut.Arguments
            arguments = arguments.replace("\"","")  #先處理 "" 的符號
            # print(arguments)
            if( Targetpath == "C:\Program Files\Google\Chrome\Application\chrome.exe"):
                profile_para_list.append(arguments)
                profile_name_list.append(file)
    else :
        profile_name_list,profile_para_list = read_profile_file()

    return browser_num, profile_name_list, profile_para_list

def read_config():
    #參數
    # browser_num = 1
    # browser_num_once = 1
    # task_mode = -1
    # multi_web_mode = 1
    # multi_profile_mode = 0
    # multi_web_delete_mode = 0
    # chapter_num = 1
    # window_select_profile_mode = 0
    # rest_profile_mode = 0


    #開檔，讀出設定資訊
    with open("./Config.txt" , mode = 'r',encoding="utf-8") as read_text: 
        for line in read_text:
            if(line[0] == "#" or line[0] == "\n"):
                continue
            else:
                line_element = line.split('=',1) #用空白鍵將字串分開 (將字串分兩段)
                line_element = [i.strip() for i in line_element]    #字串空白處理(前後空白)

                #對比可能的字串
                if(line_element[0] == "browser_num"):
                    browser_num = int(line_element[1])

                elif(line_element[0] == "browser_num_once"):
                    browser_num_once = int(line_element[1])
                
                elif(line_element[0] == "task_mode"):
                    task_mode = int(line_element[1])   

                elif(line_element[0] == "multi_web_mode"):
                    multi_web_mode = int(line_element[1])     

                elif(line_element[0] == "multi_profile_mode"):
                    multi_profile_mode = int(line_element[1])      

                elif(line_element[0] == "multi_web_delete_mode"):
                    multi_web_delete_mode = int(line_element[1])    

                elif(line_element[0] == "chapter_num"):
                    chapter_num = int(line_element[1])   

                elif(line_element[0] == "window_select_profile_mode"):
                    window_select_profile_mode = int(line_element[1])   

                elif(line_element[0] == "rest_profile_mode"):
                    rest_profile_mode = int(line_element[1])   
                    print(rest_profile_mode)
                    

    #Chrome_base_address
    user_name = os.environ.get('USERNAME') #get username,ex:JasonHong
    Chrome_base_address = 'C:/Users/' +  user_name + '/AppData/Local/Google/Chrome/'            #'C:/Users/JasonHong/AppData/Local/Google/Chrome/'


    return browser_num, browser_num_once, task_mode, multi_web_mode, multi_web_delete_mode, multi_profile_mode, window_select_profile_mode, rest_profile_mode , Chrome_base_address, user_name, chapter_num
    
    
    
    