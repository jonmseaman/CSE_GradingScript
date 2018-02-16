# See https://superuser.com/questions/17612/batch-convert-word-documents-to-pdfs
$Word=New-Object -ComObject Word.Application

$Files=Get-ChildItem ".\*.docx"

ForEach ($File In $Files) {
    $Document=$Word.Documents.Open($File.FullName)

    $Name=($Document.FullName).Replace("docx", "pdf")

    $Document.SaveAs([ref] $Name, [ref] 17)
    $Document.Close()
}

$Word.Quit()
