# coding=utf-8

# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout as auth_logout

from outsidemerch.decorators import render_to


# def logout(request):
#     """Logs out user"""
#     auth_logout(request)
#     return redirect('/')


def context(**extra):
    return dict(**extra)


@render_to('outsidemerch/overall.html')
def root(request):
    """Home view"""
    greetings = {"en": "Hi", "ja": u"ばか", "zh": u"嗨", "es": u"¡Hola!"}
    return context(greeting=greetings)


@render_to('outsidemerch/stages.html')
def stages(request):
    """Stage view"""
    greetings = {"en": "Hi", "ja": u"ばか", "zh": u"嗨", "es": u"¡Hola!"}
    return context(greeting=greetings)