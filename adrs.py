import os
try:
    def check_path_exists(path):
        # بررسی وجود مسیر
        if os.path.exists(path):
            print(f"مسیر '{path}' در سیستم شما وجود دارد.")
        else:
            ...

    # دریافت مسیر از کاربر
    user_path = input("لطفاً مسیر فایل یا پوشه را وارد کنید: ")
    check_path_exists(user_path)
except:
    print(f"مسیر در سیستم شما وجود ندارد.")