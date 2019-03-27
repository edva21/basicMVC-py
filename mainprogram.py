from model import ModelBasic
from controller import Controller
from view import View

def mainprogram():
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    c = Controller(ModelBasic(my_items), View())
    ##c.show_custom_message('Show Objects')
    c.show_items()
    ##c.show_custom_message('Show Objects with bullet poits')
    c.show_items(bullet_points=True)
    ##c.show_custom_message('Show chocolate')
    c.show_item('chocolate')
    ##c.show_custom_message('Show bread')
    c.show_item('bread')
    ##c.show_custom_message('insert bread')
    c.insert_item('bread', price=1.0, quantity=5)
    #c.show_custom_message('insert chocolate')
    c.insert_item('chocolate', price=2.0, quantity=10)
    #c.show_custom_message('show chocolate')
    c.show_item('chocolate')
    #c.show_custom_message('update milk')
    c.update_item('milk', price=1.2, quantity=20)
    #c.show_custom_message('update ice cream')
    c.update_item('ice cream', price=3.5, quantity=20)
    #c.show_custom_message('delete dish')
    c.delete_item('fish')
    #c.show_custom_message('delete bread')
    c.delete_item('bread')
if __name__ == '__main__':
    mainprogram()    