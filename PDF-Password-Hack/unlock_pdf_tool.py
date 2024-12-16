import PyPDF2

# Open the PDF file
pdf_file = open('abc locked.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Iterate over the possible date combinations
for i in range(1, 7):  # Year
    for j in range(1, 13):  # Month
        for k in range(1, 32):  # Day

            DOYear = "200" + str(i)
            DOMonth = f"{j:02d}"  # Ensure two digits for month
            DODate = f"{k:02d}"   # Ensure two digits for day

            password = f"{DODate}/{DOMonth}/{DOYear}"
            print(f"Trying password: {password}")

            try:
                # Attempt to decrypt the PDF with the password
                pdf_reader.decrypt(password)
                # Try to read the first page to check if decryption was successful
                try:
                    pdf_reader.pages[0]
                    print(f'Success! The password is: {password}')
                    break
                except:
                    continue
            except:
                continue
        else:
            continue
        break
else:
    print('Password not found in the provided range.')
