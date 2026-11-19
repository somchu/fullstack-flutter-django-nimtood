#กำหนด environment ของ python ให้กับโปรเจกต์
- เนื่องจากแต่ละโปรเจกต์อาจใช้ environment ไม่เหมือนกัน 
ดังนั้นเราจึงต้องสร้าง environment ของ python ให้กับแต่ละโปรเจกต์
```
mkdir week01 && cd week01 //สร้างโฟลเดอร์งาน
python -m venv .venv //.venv คือชื่อ environment
.venv\Scripts\activate //activate environment (จะมีชื่อ environment นำหน้า prompt)
pip install <ชื่อ package> //ติดตั้ง package
pip list //ดูรายชื่อ package
pip freeze > requirements.txt //บันทึกรำยกำร package ลงในไฟล์ requirement.txt
pip install -r requirements.txt //ติดตั้ง package จากไฟล์ requirement.txt
deactivate //ออกจาก environment