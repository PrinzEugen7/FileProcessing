Sub Sample1()
    Dim buf As String
    Open "data.txt" For Input As #1
        Line Input #1, buf
        MsgBox buf
    Close #1
End Sub
