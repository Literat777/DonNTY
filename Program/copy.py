def onCopy(self, event):
        //Копировать в буфер обмена
		
        self.dataObj = wx.TextDataObject()
        self.dataObj.SetText(self.text.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.dataObj)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")
