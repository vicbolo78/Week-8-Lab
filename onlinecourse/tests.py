import unittest

from django.test import TestCase

class TestQuestion(unittest.TestCasel):
    def test_is_get_score(self, selected_ids):
        self.assertNotEqual(all_answers = self.choice_set.filter(is_correct=True).count()
        self.assertEqual(selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False
        

       
if __name__=='__main__':
    unittest.main()
