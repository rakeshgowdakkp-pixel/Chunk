file = open ("sample.txt" , "r" , encoding ="utf-8")
contents = file.read()
file.close()

print(contents)

print(len(contents))

chunk_size = 150
chunks = []

for i in range(0, len(contents), chunk_size):
    chunk = contents[i: i+chunk_size]
    chunks.append(chunk)

for i, chunk in enumerate(chunks)  :
    print(f"Chunk {i+1} :")
    print(chunk)


