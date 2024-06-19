from views.view import View
from presenter import Presenter

def main():
    view = View()
    presenter = Presenter(view)

if __name__ == "__main__":
    main()
