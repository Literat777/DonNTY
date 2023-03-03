def cut():
    t_input.clipboard_clear()  # Очистить буфер обмена
    t_input.clipboard_append(t_input.get(1.0, END))  # Скопировать текст в буфер обмена
    t_input.delete(1.0, END)