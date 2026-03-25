# 1. 使用官方的小型 Python 映像檔作為基礎
FROM python:3.9-slim

# 2. 設定貨櫃內的工作目錄
WORKDIR /app

# 3. 把你電腦（或倉庫）裡的程式碼複製到貨櫃裡
COPY rtp_test.py .

# 4. 告訴貨櫃：一啟動就要執行這行指令
CMD ["python", "rtp_test.py"]
