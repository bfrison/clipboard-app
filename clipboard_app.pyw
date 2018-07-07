import sys
#Add the path to the clipboard_utils module in the line below if in different folder
#sys.path.append(r'')

import clipboard_utils

tk = clipboard_utils.create_GUI()
tk.mainloop()
