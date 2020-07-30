'''购物车测试用例类'''
import time
import unittest
from page.shoppingcart_page import ShoppingCartPage
from test_case.base_test import BaseTestCase


class ShoppingCartTestCase(BaseTestCase):
    '''购物车测试用例类'''
    def test_1shopping_cart_flow(self):
        '''一般购物流程'''
        cart = ShoppingCartPage(self.driver)
        cart.shopping_cart_flow()
        # self.assertEqual(True, False)

    def test_2modify_product_num(self):
        '''修改购物车商品数量'''
        cart = ShoppingCartPage(self.driver)
        cart.modify_product_num_flow(2)
        cart.edit_product_num(2,'sub')

    def test_3clear_shoppingcart(self):
        '''清除购物车'''
        cart = ShoppingCartPage(self.driver)
        cart.get_in_shoppingcart()
        cart.delete_button()
        cart.ensure_delete()

    def test_4add_recommend_product(self):
        '''添加推荐商品'''
        cart = ShoppingCartPage(self.driver)
        cart.get_in_shoppingcart()
        cart.swipe_to('down')
        time.sleep(1)
        cart.add_recommend_product(1)
        cart.add_recommend_product(2)


if __name__ == '__main__':
    unittest.main()
