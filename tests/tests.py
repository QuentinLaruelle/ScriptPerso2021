import unittest

import inventaire


class Product(unittest.TestCase):
    """
    author : Quentin Laruelle
    Date : December 2022
    """
    def test_change_name(self):
        """
        This method tests the change_name method
        """
        self.assertEqual(inventaire.Product.change_name(self, 'fabian'), None, 'Devrait retourner None')
        self.assertEqual(inventaire.Product.change_name(self,'' ), None , 'Devrait retourner None')
        self.assertEqual(inventaire.Product.change_name(self, 125), False, 'Devrait retourner False')
        self.assertEqual(inventaire.Product.change_name(self, bool), False, 'Devrait retourner False')

    def test_change_price(self):
        """
        This method tests the change_price method
        """
        self.assertEqual(inventaire.Product.change_price(self, 'hfdklsv'), None, 'Devrait retourner None')
        self.assertEqual(inventaire.Product.change_price(self, ' '), None, 'Devrait retourner None')
        self.assertEqual(inventaire.Product.change_price(self, 4456), False, 'Devrait retourner False')
        self.assertEqual(inventaire.Product.change_price(self, bool), False, 'Devrait retourner False')

    def test_change_stock(self):
        """
        This method tests the change_stock method
        :return:
        """
        self.assertEqual(inventaire.Product.change_stock(self, 'L\'homme d\'acier'), None, 'Devrait retourner None')
        self.assertEqual(inventaire.Product.change_stock(self, ' '), None, 'Devrait retourner None')
        self.assertEqual(inventaire.Product.change_stock(self, 12523), False, 'Devrait retourner False')
        self.assertEqual(inventaire.Product.change_stock(self, bool), False, 'Devrait retourner False')

if __name__ == '__main__':
    unittest.main()
