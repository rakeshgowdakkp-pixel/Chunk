from pypdf import PdfReader

doc = PdfReader("sample_vmware_sop.pdf")
text = ""

for page in doc.pages:
    text += page.extract_text()

print(text)

print(len(text))

chunk_size = 50
chunks =[]

for i in range(0, len(text), chunk_size):
    chunk = text[i: i+chunk_size]
    chunks.append(chunk)

for i, chunk in enumerate(chunks)    :
    print (f"chunk {i+1} :")
    print(chunk)
    print()
    