from PIL import Image

# 변환할 PNG 파일 열기
img = Image.open("money.png")

# .ico 파일로 저장
img.save("money.ico", format="ICO")