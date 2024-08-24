import requests

def download_image(url):
  """
  این تابع یک تصویر را از آدرس اینترنتی داده شده دانلود می کند و آن را در همان پوشه برنامه ذخیره می کند.

  Args:
    url: آدرس اینترنتی تصویر

  Returns:
    None
  """

  # ارسال درخواست به سرور برای دریافت تصویر
  response = requests.get(url, stream=True)

  # بررسی وضعیت درخواست
  if response.status_code == 200:
    # ایجاد نام فایل با استفاده از یک بخش از URL و پسوند مناسب
    file_name = "downloaded_image.jpg"  # یا هر نام دلخواه دیگری
    # برای استخراج پسوند از کتابخانه os.path استفاده کنید
    # import os
    # file_extension = os.path.splitext(url)[1]
    # file_name = "my_image" + file_extension

    # ذخیره تصویر در فایل
    with open(file_name, 'wb') as out_file:
      for chunk in response.iter_content(1024):
        out_file.write(chunk)
    print(f"تصویر با موفقیت دانلود شد: {file_name}")
  else:
    print("خطا در دانلود تصویر")

# دریافت آدرس تصویر از کاربر
image_url = input("لطفا آدرس تصویر را وارد کنید: ")

# فراخوانی تابع دانلود تصویر
download_image(image_url)