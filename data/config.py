from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5001491339:AAFeAZ9BG7x6PFFkYKXhCO7B8cxmgP3QaCg"
# BOT_TOKEN = "1936771362:AAHlnu9ACW27yVLcqhX52xxO3dpaD_W5mFI" # Bot toekn Test
ADMINS = ['1600170280', '1019865273', '99940983','938759596']
# ADMINS = ['915850675']# adminlar ro'yxati Test
IP = "localhost"  # Xosting ip manzili
#PAYMENTS_PROVIDER_TOKEN = '387026696:LIVE:6149b6f02dfdc60f985e6b91'
PAYMENTS_PROVIDER_TOKEN = '371317599:TEST:1656247972820'#Токен оплаты по Клик Test
OFFICE_LOCATION = [41.269655, 69.319892]
