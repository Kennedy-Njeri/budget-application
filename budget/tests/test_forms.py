from django.test import SimpleTestCase
from budget.forms import ExpenseForm


class TestForms(SimpleTestCase):

    


    def test_expense_form_no_data(self):
        form = ExpenseForm(data={})


        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)