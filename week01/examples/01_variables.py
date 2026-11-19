#ไม่ต้องประกาศชนิด — Python ดูเองจากค่าที่ใส่
name= "Somchai" 
age = 30            #ชนิดจำนวนเต็ม ไม่จำกัดขนาด
height = 172.5      #ชนิด float
is_active = True    #boolean
nothing = None      #ค่า null

#ดูชนิดของตัวแปร
print(type(age))    #result <class 'int'>

#ตอนทำงานจริงควรประกาศชนิดของตัวแปรดีกว่า
price: float = 99.5
tags: list[str] = ["python","django"]

#ถ้าไม่กำหนดชนิดของตัวแปรแต่แรก เราสามารถเปลี่ยนชนิดของตัวแปรได้ 
#โดยจะยึดค่าที่ใช้ล่าสุดเป็นประเภทตัวแปรเสมอ
x = 10
x = "ten" #แบบนี้ไม่ควรทำ

#python ไม่มี const แต่นิยมใช้ตัวพิมพ์ใหญ่
MAX_LOGIN_ATTEMPTS = 9

#multiple assignment and swap
a, b = 1, 2
a, b = b, a
print(a, b)

#การแปลงชนิด (casting)
#ใน Python ต้องพิมพ์ True / False ตัวแรกพิมพ์ใหญ่
n = int("42")
f = float("3.14")
s = str(100)
ok = bool("")

#operation
print(7/2)
print(7//2)  #หารปัดลง (floor division)
print(7%2)  #หารเอาแต่เศษ (mod)
print(2**10) #ยกกำลัง
print(7%-2)
#-7 // 2 ได้ -4 ปัดลงเสมอ ปัดไปทางลบ
#-7 % 2 ได้ 1 แต่ C# ได้ -1