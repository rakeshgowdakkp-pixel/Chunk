from docx import Document

doc = Document("Sample_word.docx")

text = ""

for para in doc.paragraphs:
    text += para.text + "\n"

print(text)    


chunk_size = 500
chunks =[]

for i in range(0, len(text) ,chunk_size):
    chunk = text[i: i+chunk_size]
    chunks.append(chunk)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print()  


    
