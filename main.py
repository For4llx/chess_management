from controllers.base import Controller
from views.base import View


def main():
    view = View()
    controller = Controller(view)
    controller.main_menu(view)

if __name__ == "__main__":
    main()
