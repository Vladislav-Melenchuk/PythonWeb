from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

def expense_list(request):
    expenses = Expense.objects.all()
    total = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'ListDo/list.html', {'expenses': expenses, 'total': total})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'ListDo/add.html', {'form': form})

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('expense_list')
