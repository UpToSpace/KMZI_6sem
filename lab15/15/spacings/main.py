import stegospacings

stegospacings.encode('mikhail', 'container.docx', 'encoded.docx')
print(stegospacings.decode('encoded.docx'))
