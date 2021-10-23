import mechanize


def checkPin():
    br = mechanize.Browser()
    response = br.open("https://itax.kra.go.ke/KRA-Portal/pinChecker.htm")
    print(response.read())

    for form in br.forms():
        print("Form name: ", form.name)
        print(form)

        print("Controls")

        for control in form.controls:
            print(control)
            print("type=%s, name=%s", control.type, control.name)


