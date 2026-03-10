import os
import kaggle
import zipfile


def download_and_extract(dataset_name,download_path):


    if not os.path.exists(download_path):
        os.makedirs(download_path)
    kaggle.api.dataset_download_files(dataset_name,path=download_path,unzip=False)

    zip_path = os.path.join(download_path,"fer2013.zip")

    with zipfile.ZipFile(zip_path,'r') as zip_ref:
        zip_ref.extractall(download_path)

    os.remove(zip_path)
    print(f"Toàn bộ ảnh nào trong thư mục:{download_path}")


def cat_ghep_anh():
    print("catghep")
    pass
def xoa_rac():
    print("..")
    pass

def tong_luc():
    download_and_extract('msambare/fer2013','./dataset')
    cat_ghep_anh()
    xoa_rac()

if __name__ == "main":
    tong_luc()
