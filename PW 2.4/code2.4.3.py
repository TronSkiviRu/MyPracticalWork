import sqlite3
import psutil
from datetime import datetime

DB_NAME = 'system_monitor.db'

def init_db():
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            cpu_usage REAL NOT NULL,
            memory_usage REAL NOT NULL,
            disk_usage REAL NOT NULL
        );
    """)
    con.commit()
    con.close()

def collect_and_save_stats():
    # Получаем показатели
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Сохраняем в БД
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
    cursor.execute("""
        INSERT INTO system_stats (timestamp, cpu_usage, memory_usage, disk_usage)
        VALUES (?, ?, ?, ?)
    """, (timestamp, cpu, memory, disk))
    con.commit()
    con.close()

    print(f"Данные сохранены: {timestamp} | CPU: {cpu}% | RAM: {memory}% | Disk: {disk}%")

def show_all_records():
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
    cursor.execute("SELECT id, timestamp, cpu_usage, memory_usage, disk_usage FROM system_stats ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    con.close()

    if not rows:
        print("Данные мониторинга отсутствуют.")
        return

    print("Записи мониторинга:")
    print(f"{'ID':<4} {'Время':<20} {'CPU %':<7} {'RAM %':<7} {'Disk %':<7}")
    for r in rows:
        print(f"{r[0]:<4} {r[1]:<20} {r[2]:<7.2f} {r[3]:<7.2f} {r[4]:<7.2f}")

def main():
    init_db()
    while True:
        print("\nСистемный монитор")
        print("1. Собрать и сохранить текущие данные")
        print("2. Показать сохранённые данные")
        print("3. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == '1':
            collect_and_save_stats()
        elif choice == '2':
            show_all_records()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте еще раз.")


if __name__ == '__main__':
    main()