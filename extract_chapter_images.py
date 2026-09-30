import fitz
import os
src = 'source/Peddie P. The History of the GPU - Steps to Invention 2022.pdf'
doc = fitz.open(src)
os.makedirs('source/en/images', exist_ok=True)
seen = set()
count = 0
for pno in range(28, 58):
    for img in doc[pno].get_images(full=True):
        xref = img[0]
        if xref in seen:
            continue
        seen.add(xref)
        data = doc.extract_image(xref)
        count += 1
        name = f'chapter-01-fig-{count:02d}.{data["ext"]}'
        with open(os.path.join('source/en/images', name), 'wb') as f:
            f.write(data['image'])
        print(name, 'PDF page', pno + 1)
print('extracted', count)
