from django.shortcuts import render
from django.views import View
from .models import Item, Comment, Reaction
from django.http import HttpResponseRedirect

# Create your views here.

class ItemView(View):

    def select_reaction(self, requested_item, selection):
        new_reaction = Reaction.objects.get(reaction=selection)
        got_item = Item.objects.get(item=requested_item.capitalize())
        got_item.reactions = new_reaction
        got_item.save()

    def get(self, request, requested_item):
        try:
            got_item = Item.objects.get(item=requested_item.capitalize()) # in future similar cases, the source of the following error shoud be found: item.models.Item.DoesNotExist: Item matching query does not exist.
        except Item.DoesNotExist:
            got_item = None
        comments = Comment.objects.filter(item=got_item)
        return render(request, 'item/item.html', {'item':got_item, 'comments':comments})
    
    def post(self, request, requested_item):
        if request.POST.get('new-comment'):
            new_comment = Comment(
                comment=request.POST.get('new-comment'),
                item=Item.objects.get(item=requested_item.capitalize())
                )
            new_comment.save()
        if request.POST.get('item-reaction'):
            if request.POST.get('item-reaction') == "1":
                self.select_reaction(requested_item, True)
            if request.POST.get('item-reaction') == "0":
                self.select_reaction(requested_item, False)
        if request.POST.get('comment-reaction'):
            got_comment = Comment.objects.get(
                id=request.POST.get('comment-reaction').split(',')[1]
                )
            if request.POST.get('comment-reaction').split(',')[0] == '1':
                new_reaction = Reaction.objects.get(reaction=True)
            if request.POST.get('comment-reaction').split(',')[0] == '0':
                new_reaction = Reaction.objects.get(reaction=False)
            got_comment.reactions = new_reaction
            got_comment.save()
        return HttpResponseRedirect(f"/{requested_item}")


class WelcomePageView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'item/welcome-page.html', {'items':items})
    def post(self, request):
        item = Item(item=request.POST['new-item'])
        item.save()
        return HttpResponseRedirect('/')