from django.shortcuts import render, redirect
from django.views.generic import View
from authentication.models import User
from followers.models import UserFollows


class FollowersView(View):

    def get(self, request):
        if not request.user.is_anonymous:
            followed_users = UserFollows.objects.filter(user=request.user)
            excluded_ids = [u.followed_user.id for u in followed_users]
            excluded_ids.append(request.user.id)
            i_follow_users_ids = [u.followed_user.id for u in followed_users]
            i_follow_users = []
            if len(i_follow_users_ids):
                i_follow_users = User.objects.filter(id__in=i_follow_users_ids)
            followable_users = User.objects.exclude(id__in=excluded_ids)
            return render(request, 'followers/list_view.html', {
                'followable_users': followable_users,
                'i_follow_users': i_follow_users
                })

    def post(self, request, id):
        if not request.user.is_anonymous:
            user_follow = UserFollows()
            user_follow.user = User.objects.get(id=request.user.id)
            user_follow.followed_user = User.objects.get(id=id)
            if request.POST.get("form") == 'follow':
                user_follow.save()
            elif request.POST.get("form") == 'unfollow':
                was_followed_user = User.objects.get(id=id)
                unfollow_user = UserFollows.objects.get(
                    user=request.user,
                    followed_user=was_followed_user
                    )
                unfollow_user.delete()
            return redirect('followers_list')
