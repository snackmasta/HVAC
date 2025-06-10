import pypandoc

input_file = r'c:\Users\Legion\Desktop\HVAC\docs\report\hvac-09-software-jaringan.md'
output_file = r'c:\Users\Legion\Desktop\HVAC\docs\report\hvac-09-software-jaringan.docx'

output = pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
print(f"Converted {input_file} to {output_file}")
