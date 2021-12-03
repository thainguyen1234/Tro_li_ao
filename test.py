from gtts import gTTS
from playsound import playsound
import os
import random


# print("*    *  *****      *")
# print("*    * *     *    * *")
# print("****** *     *   *****")
# print("*    * *     *  *     *")
# print("*    *  *****  *       *")

text = "HEY, CHÀO MỪNG ĐẾN VỚI TRỢ LÍ ẢO FAKE!!!"

print(text)
tts = gTTS(text,lang="vi", slow=True)
tts.save("a.mp3")
playsound('a.mp3', True)
os.remove("a.mp3")

def Vi(l, text):
	f = str(random.randint(1,1000000000000000)) + ".mp3" 

	tts = gTTS(text,lang=l, slow=True)
	tts.save(f)
	playsound(f, True)
	os.remove(f)	


def En(l, text):
	f = str(random.randint(1,1000000000000000)) + ".mp3" 

	tts = gTTS(text,lang=l, slow=True)
	tts.save(f)
	playsound(f, True)
	os.remove(f)

l = input("Chọn ngôn ngữ(vi/ en): ")
if l == "vi" or l == "en":
	pass
else:
	l = input("Chọn ngôn ngữ(vi/ en): ")


isRunning = True	
while isRunning:
	text = input("Nhập câu mà bạn muốn nói: ")
	if text == "stop":
		break

	if text == "back":
		l = input("Chọn ngôn ngữ(vi/ en): ")
		if l == "vi" or l == "en":
			pass
		else:
			l = input("Chọn ngôn ngữ(vi/ en): ")


	if l == "en":
		if text == "stop":
			break
		if text == "back":
			pass
		else:
			En(l, text)
			
	elif l == "vi":
		if text == "stop":
			break
		if text == "back":
			pass
		else:
			Vi(l, text)
	else:
		print("OHHH, đã có lỗi, hãy BACK")
		Vi("vi","Ấu Ầu, đã có lỗi, hãy BACK")

