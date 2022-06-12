import pyautogui as pag

width_of_screen, height_of_screen = pag.size()

def appuyez_un_cle(les_cles: list):
    for i in les_cles:
        pag.keyDown( i )
    for i in les_cles:
        pag.keyUp( i )

if __name__ == "__main__":
    appuyez_un_cle(["WIN", "r"])
    appuyez_un_cle(["c", "m", "d", "enter"])


    pag.moveTo(width_of_screen/2, height_of_screen/2)

    pag.leftClick()

    directeur = "\"New Folder 1" #c'est le path pour le directeur qui sera efface
    pag.typewrite("del "+ directeur)
    appuyez_un_cle(["enter"])

    pag.typewrite("y")
    appuyez_un_cle(["enter"])

    pag.typewrite("rmdir " + directeur)
    appuyez_un_cle(["enter"])
