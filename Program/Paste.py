def past():
    clipboard_text = root.clipboard_get()
    t_input.insert('1.0', clipboard_text)