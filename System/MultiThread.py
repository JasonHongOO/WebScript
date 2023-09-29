import os
import time
import shutil
from tqdm import tqdm
from pathlib import Path

def multi_thread_file_delete(browser_num,Chrome_base_address,profile_para_list):
    def multi_thread_dir_delete(src):
        def delete_folder(src):
            total_size = sum(f.stat().st_size for f in src.glob('**/*') if f.is_file())
            with tqdm(total=total_size, unit='bytes', unit_scale=True, desc='delete') as pbar:
                for root, dirs, files in os.walk(src, topdown=False):
                    for name in files:
                        file_path = os.path.join(root, name)
                        try:
                            pbar.update(os.path.getsize(file_path))
                            os.remove(file_path)
                        except OSError:
                            pass  # 可能某些目錄因權限等原因無法删除，略過
                    for name in dirs:
                        dir_path = os.path.join(root, name)
                        try:
                            os.rmdir(dir_path)
                        except OSError:
                            pass  # 可能某些目錄因權限等原因無法删除，略過
                try:
                    os.rmdir(src)
                except OSError:
                    pass  # 可能某些目錄因權限等原因無法删除，略過
        delete_folder(src)

    BaseAddress = Chrome_base_address
    for i in range(browser_num):
        TargetAddress = BaseAddress + profile_para_list[i].split('=')[1] + '/'

        #查看資料夾是否已存在
        check = os.path.exists(TargetAddress)

        if(check == True):
            # shutil.rmtree(TargetAddress)
            TargetAddress = Path(TargetAddress)
            multi_thread_dir_delete(TargetAddress)
            print("delete folder %s success"%profile_para_list[i].split('=')[1])

def multi_thread_preparations(browser_num,Chrome_base_address,profile_para_list):
    def multi_thread_dir_copy(src, dest):
        def copy_folder(src, dest):
            # 獲取所有文件的總大小
            # 使用 src.glob('**/*') 以獲取所有子目錄的資訊，並使用 f.is_file 確定是檔案，而不是s資料夾、軟連結等等，以正確的計算整個資料夾的實際大小
            total_size = sum(f.stat().st_size for f in src.glob('**/*') if f.is_file())
            
            # 使用 shutil.copytree 覆制整個文件夾，並在覆制每個文件時顯示進度條
            with tqdm(total=total_size, unit='bytes', unit_scale=True, desc='Copying') as pbar:
                shutil.copytree(src, dest, dirs_exist_ok=True, copy_function=copy_with_progress(pbar.update))
                pbar.update(total_size - pbar.n)  # 確保進度條顯示完整
            
        def copy_with_progress(progress_callback):
            #透過 "隱式傳遞" 來傳定 src、dest
            def copy_with_progress_callback(src, dest):
                shutil.copy2(src, dest)
                progress_callback(shutil.os.path.getsize(src))
            
            return copy_with_progress_callback
        
        copy_folder(src, dest)

    BaseAddress = Chrome_base_address
    for i in range(browser_num):
        UserDataAddress = BaseAddress + 'User Data/'
        UserDataTargetFolder = UserDataAddress + profile_para_list[i].split('=')[1]
        UserDataTargetFile = UserDataAddress + 'Local State'
        TargetAddress = BaseAddress + profile_para_list[i].split('=')[1] + '/'
        TargetAddressFolder = TargetAddress + profile_para_list[i].split('=')[1]
        TargetAddressFile = TargetAddress + 'Local State'

        #查看資料夾是否已存在
        check = os.path.exists(TargetAddress)
        
        #如果檔案、資料夾不存在
        if(check == False):
            print("folder %s not found."%profile_para_list[i].split('=')[1])
            print("create folder %s "%profile_para_list[i].split('=')[1])
            #創建資料夾
            # os.mkdir(TargetAddress)

            try:
                #複製檔案
                # shutil.copytree(UserDataTargetFolder,TargetAddressFolder) #這邊會幫忙創建
                UserDataTargetFolder = Path(UserDataTargetFolder)
                TargetAddressFolder = Path(TargetAddressFolder)
                multi_thread_dir_copy(UserDataTargetFolder,TargetAddressFolder)
                shutil.copy(UserDataTargetFile,TargetAddressFile)
            except:      
                print("create folder error")
                #刪除已創建的檔案

                #查看資料夾是否已存在
                check = os.path.exists(TargetAddress)
                if(check == True):
                    shutil.rmtree(TargetAddress)
                    print("delete folder %s success"%profile_para_list[i].split('=')[1])
                else:
                    print("檔案創建失敗，但是資料夾也不存在")

                print("exit after 10 seconds")
                time.sleep(10)
                exit(1)             

            print("create folder %s success"%profile_para_list[i].split('=')[1])
        else:
            print("folder %s alredy exist."%profile_para_list[i].split('=')[1])
