import pyautogui as pag

width_of_screen, height_of_screen = pag.size()

def appuyez_un_cle(les_cles: list):
    for i in les_cles:
        pag.keyDown( i )
    for i in les_cles:
        pag.keyUp( i )

if __name__ == "__main__":
    appuyez_un_cle(["CTRL", "alt", "t"])

    pag.countdown(3)
    pag.moveTo(width_of_screen/2, height_of_screen/2)
    pag.leftClick()

    directory = "\"New Folder 1\"/" #c'est le path pour le directeur qui sera efface
    # ensemble avec tout ses fichiers et les directeurs interieur
    pag.typewrite("rm -r " + directory)
    appuyez_un_cle(["enter"])
