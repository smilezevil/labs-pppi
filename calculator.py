import os
import math
import datetime
import re
import tkinter as tk
from tkinter import messagebox
# ВИПРАВЛЕНО: Імпортуємо ttk для доступу до стилів та віджетів
from tkinter import ttk
from tkinter.ttk import Separator, Style, Button as TtkButton, Label as TtkLabel, Frame as TtkFrame

INPUT_FILE = "Input data.txt"
OUTPUT_FILE = "Output data.txt"
SESSION_LOG_FILE = "Session log.txt"

Doroftei

main
def log_action(action_text, is_start=False, is_end=False):

    mode = 'w' if is_start else 'a'

    action_num = 1
    if not is_start and os.path.exists(SESSION_LOG_FILE):
        try:
            with open(SESSION_LOG_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                valid_lines = [line for line in lines if line.strip()]
                if valid_lines:
                    last_line = valid_lines[-1].strip()
                    match = re.search(r'Дія (\d+):', last_line)
                    if match:
                        action_num = int(match.group(1)) + 1
        except:
            action_num = 1

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] Дія {action_num}: {action_text}"

    try:
        with open(SESSION_LOG_FILE, mode, encoding='utf-8') as f:
            f.write(log_entry + '\n')
    except Exception as e:
        print(f"Помилка логування: {e}")


def import_data_from_file():

    log_action("обрано «Імпортувати вхідні дані»")

    try:
        if not os.path.exists(INPUT_FILE) or os.path.getsize(INPUT_FILE) == 0:
            raise ValueError("Файл порожній, введіть дані")

        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        if len(lines) < 2:
            raise ValueError("Файл містить недостатньо параметрів.")

        param1 = float(lines[0])
        param2 = float(lines[1])

    except ValueError as ve:
        raise ValueError("Недопустимі значення введених параметрів") from ve

    except Exception as e:
        raise Exception(f"Помилка читання файлу: {e}") from e

    else:
        return param1, param2


def perform_calculation(param1, param2, operation):
 Laptiuk
    """Виконує арифметичну дію (if..elif) та обробляє ZeroDivisionError."""
    log_action(f"Обрано арифметичну операцію «{operation}»")
    log_action("Обрано «Обчислити вираз»")
    log_action(f"обрано арифметичну операцію «{operation}»")
    log_action("обрано «Обчислити вираз»")
    main

    result = None

    if operation == '+':
        result = param1 + param2
    elif operation == '-':
        result = param1 - param2
    elif operation == '*':
        result = param1 * param2
    elif operation == '/':
        if param2 == 0:
            raise ZeroDivisionError("Ділення на 0 заборонено")
        result = param1 / param2
    elif operation == '^':
        result = math.pow(param1, param2)
    else:
        raise ValueError("Невідома операція")

    return result


def export_result(param1, param2, operation, result):
    output_line = f"{param1} {operation} {param2} Результат: {result}"

    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(output_line + '\n')
        log_action("обрано «Експортувати результат у файл»")
    except Exception as e:
        raise Exception(f"Помилка при записі результату: {e}")

    return output_line


 Doroftei
main
class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("ЛР №4, Завдання 33")
        master.geometry("550x500")

        # Налаштування стилів ttk для кращого вигляду на macOS
        style = Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'), foreground='#333333')
        style.configure('Big.TButton', font=('Arial', 12, 'bold'))

        log_action("Додаток запущено", is_start=True)

        self.param1 = None
        self.param2 = None
        self.current_result = None
        self.current_operation = tk.StringVar(value='+')

        self.data_display = tk.StringVar(value="Параметр 1: -\nПараметр 2: -")
        self.result_display = tk.StringVar(value="Очікування обчислення...")



        main_frame = TtkFrame(master, padding="15 15 15 15")
        main_frame.pack(fill='both', expand=True)


        TtkLabel(main_frame, text="ВХІДНІ ДАНІ", style='Header.TLabel').pack(pady=10)


        TtkButton(main_frame, text="Імпортувати вхідні дані", command=self.handle_import, style='Big.TButton').pack(
            fill='x', pady=8)

        tk.Label(main_frame, textvariable=self.data_display, justify=tk.CENTER, fg='#007BFF',
                 font=('Courier', 12)).pack(pady=(5, 15))

        Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)


        TtkLabel(main_frame, text="Оберіть арифметичну дію (Radiobutton):", style='Header.TLabel').pack(pady=10)

        op_frame = TtkFrame(main_frame)
        op_frame.pack(pady=10)


        operations = ['+', '-', '*', '/', '^']
        for op in operations:
            tk.Radiobutton(op_frame, text=op, variable=self.current_operation, value=op,
                           indicatoron=0, width=5, height=2, font=('Arial', 12, 'bold'),
                           bg='#cccccc', selectcolor='#007BFF').pack(side=tk.LEFT, padx=5)

        Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)

        # Секція 3: Обчислення та Експорт
        TtkButton(main_frame, text="ОБЧИСЛИТИ ВИРАЗ", command=self.handle_calculate, style='Big.TButton').pack(fill='x',
                                                                                                               pady=10)

        TtkLabel(main_frame, text="РЕЗУЛЬТАТ:", style='Header.TLabel').pack(pady=(5, 0))
        tk.Label(main_frame, textvariable=self.result_display, fg='#FF5722', font=('Courier', 14, 'bold'),
                 wraplength=500).pack(pady=10)

        TtkButton(main_frame, text="Експортувати результат у файл", command=self.handle_export,
                  style='Big.TButton').pack(fill='x', pady=8)

        master.protocol("WM_DELETE_WINDOW", self.on_closing)


    def handle_import(self):
        try:
            self.param1, self.param2 = import_data_from_file()
            self.data_display.set(f"Параметр 1: {self.param1}\nПараметр 2: {self.param2}")
            messagebox.showinfo("Імпорт", "Дані успішно імпортовано.")
        except ValueError as ve:
            messagebox.showerror("Помилка вхідних даних", str(ve))
            self.param1, self.param2 = None, None
            self.data_display.set("Помилка: введіть коректні дані")
        except Exception as e:
            messagebox.showerror("Помилка файлової системи", str(e))
            self.param1, self.param2 = None, None
            self.data_display.set("Помилка: не вдалося прочитати файл")

    def handle_calculate(self):
        if self.param1 is None or self.param2 is None:
            messagebox.showwarning("Обчислення", "Спочатку імпортуйте вхідні дані.")
            return

        operation = self.current_operation.get()

        try:
            result = perform_calculation(self.param1, self.param2, operation)
            self.current_result = result

            output_line = f"{self.param1} {operation} {self.param2} Результат: {result}"
            self.result_display.set(output_line)

        except ZeroDivisionError as zde:
            messagebox.showerror("Помилка обчислення", str(zde))
            self.result_display.set(f"Помилка: {str(zde)}")
            self.current_result = None
        except Exception as e:
            messagebox.showerror("Помилка обчислення", str(e))
            self.result_display.set(f"Помилка: {str(e)}")
            self.current_result = None

    def handle_export(self):
        if self.current_result is None:
            messagebox.showwarning("Експорт", "Немає результату для експорту. Спочатку обчисліть вираз.")
            return

        operation = self.current_operation.get()

        try:
            export_result(self.param1, self.param2, operation, self.current_result)
            messagebox.showinfo("Експорт",
                                f"Результат успішно записано у {OUTPUT_FILE} та оновлено {SESSION_LOG_FILE}.")
        except Exception as e:
            messagebox.showerror("Помилка експорту", str(e))

    def on_closing(self):
        log_action("додаток закрито", is_end=True)
        self.master.destroy()


if __name__ == "__main__":
    if not os.path.exists(INPUT_FILE):
        try:
            with open(INPUT_FILE, 'w', encoding='utf-8') as f:
                f.write("10.5\n")
                f.write("2.0\n")
        except Exception:
            pass

    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()