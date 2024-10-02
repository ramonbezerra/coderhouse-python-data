import re

# txt = "Lorem Ipsum is simply dummy text of the printing email@email.com.br and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type mary@mailing.com and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets joe@mail.com containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# # [\w\.-]+@[\w\.-]+\.[\w]{2,3}

# matches = re.findall("([a-z.0-9]+@[a-z.0-9]+)", txt)

# print(matches)

data = "Code review concluído no dia 31/05/2021 e Merge feito no dia 23/07/2021 e Deploy feito no dia 12/10/2022"

matches = re.findall("(\d{2}\/(0[456]|0[789])\/\d{4})", data)

print(matches)