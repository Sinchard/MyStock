from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from base.models import Wordbook, Category


class CategoryList(ListView):
    model = Category


class CategoryCreate(CreateView):
    model = Category
    fields = ['name', 'description']


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'description']


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


'''
def show_wordbook(request):
    wordbooks = wordbook.objects.all()
    context_dict = {}
    context_dict["wordbooks"] = wordbooks
    return render(request, 'base/wordbook.html', context_dict)


def add_wordbook(request):
    form = wordbookForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = wordbookForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back to the index view.
            return redirect('/base/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'base/add_wordbook.html', {'form': form})
'''