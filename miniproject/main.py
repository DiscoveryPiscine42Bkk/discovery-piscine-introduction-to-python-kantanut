def show_menu():
    print("\n---ฟาร์มทุเรียน---")
    print("1.เพิ่มงานในฟาร์ม")
    print("2.เเสดงรายการทั้งหมด")
    print("3.ลบงาน")
    print("4.สรุปจำนวนงานในเเต่ละประเภท")
    print("5.ออกจากโปรมเเกรม")

def add_task():
    print("\n---ฟาร์มทุเรียน---")
    print("1.เลือกต้นพันธุ์")
    print("2.ปลูกให้เหลือดินเดิม")
    print("3.ใช้ไม้ค้ำป้องกันการโยก")
    print("4.รดน้ำวันละครั้ง")
    print("5.รากเดินเเล้วจึงเติมปุ๋ย")
    print("7.พรางให้เเสงทุเรียน")
    print("8.ให้ปุ๋ยทางใบเสริม")
    print("9.ใช้ไตรโคเดอร์มาปกป้องราก")

def menu():
    while true:
        print("\n====ฟาร์มทุเรียน====")
        print("1.เพิ่มงานในฟาร์ม")
        print("2.เเสดงรายการทั้งหมด")
        print("3.ลบงาน")
        print("4.สรุปจำนวนงานในเเต่ละประเภท")
        print("5.ออกจากโปรมเเกรม")
        choice = input("เลือกเมนู [1-5]: ")
    
    job_choice = input("เลือกหมายเลขงาน (1-9): ")

    job_dict = {
        "1": "เลือกต้นพันธุ์อายุไม่เกิน 1 ปี",
        "2": "ปลูกให้เหลือดินเดิม ประมาณ 1 นิ้ว",
        "3": "ใช้ไม้ค้ำป้องกันต้นโยก",
        "4": "รดน้ำวันละครั้ง",
        "5": "รากเดินแล้วจึงเริ่มให้ปุ๋ย",
        "6": "คลุมโคนรักษาความชื้น",
        "7": "พรางแสงให้ทุเรียน",
        "8": "ให้ปุ๋ยทางใบเสริม",
        "9": "ใช้ไตรโคเดอร์มาปกป้องราก"
    }
    if job_choice in job_dict:
        name = job_dict[job_choice]
    elif job_choice == "9":
        name = input("ป้อนชื่องานที่ต้องการเพิ่ม: ")
    else:
        print("❌ เลือกไม่ถูกต้อง")
        return

    print("เลือกประเภทงาน:")
    print("1. 9 วิธีปลูกทุเรียนให้รอด")
    category_choice = input("เลือก (1): ")
    category = "9 วิธีปลูกทุเรียนให้รอด" if category_choice == "1" else "ไม่ใช่วิธีปลูกทุเรียน"

    date_created = datetime.now().strftime("%Y-%m-%d")

    farm_tasks.append({
        "name": name,
        "category": category,
        "date": date_created
    })

    print(f"➕ เพิ่มงาน '{name}' เรียบร้อยแล้ว (วันที่: {date_created})")

def list_tasks():
    if not farm_tasks:
        print("🔍 ยังไม่มีงานในระบบ")
    else:
        print("\n📋 รายการงานทั้งหมด:")
        for i, task in enumerate(farm_tasks, start=1):
            print(f"{i}. {task['name']} ({task['category']}) - เพิ่มเมื่อ: {task['date']}")

def delete_task():
    list_tasks()
    try:
        index = int(input("ป้อนหมายเลขงานที่ต้องการลบ: ")) - 1
        if 0 <= index < len(farm_tasks):
            removed = farm_tasks.pop(index)
            print(f"🗑 ลบงาน: {removed['name']} แล้วเรียบร้อย")
        else:
            print("❌ ไม่พบงานหมายเลขนั้น")
    except ValueError:
        print("⚠️ โปรดใส่ตัวเลขเท่านั้น")

def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1

    print("\n📊 สรุปจำนวนงาน:")
    for cat, count in summary.items():
        print(f"- {cat}: {count} งาน")

while True:
    show_menu()
    choice = input("เลือกเมนู (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("👋 ออกจากโปรแกรมแล้ว")
        break
    else:
        print("❌ โปรดเลือกเมนู 1-5 เท่านั้น")