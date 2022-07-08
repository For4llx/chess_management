from controllers.base import Controller
from views.base import View

def main():
    view = View()
    controller = Controller(view)
    controller.main_menu(view)

main()
