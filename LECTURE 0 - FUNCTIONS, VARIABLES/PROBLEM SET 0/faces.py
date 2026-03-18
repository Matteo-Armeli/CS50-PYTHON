#with convert
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    faces = input("")
    print(convert(faces))

main()

#simplest version without convert

faces = input()
faces = faces.replace(":)", "🙂")
faces = faces.replace(":(", "🙁")
print(faces)