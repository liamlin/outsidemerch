# coding=utf-8

import os
import json
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout as auth_logout

from outsidemerch.decorators import render_to


# def logout(request):
#     """Logs out user"""
#     auth_logout(request)
#     return redirect('/')


JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lineup_2014_new.json'))
json_data=open(JSON_PATH)

lineups = json.load(json_data)
json_data.close()


def context(**extra):
    return dict(**extra)


@render_to('outsidemerch/overall.html')
def root(request):
    """Home view"""
    return context(lineups=lineups)


@render_to('outsidemerch/stages.html')
def stages(request):
    """Stage view"""
    return context(lineups=lineups)