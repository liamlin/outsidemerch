# coding=utf-8
from datetime import time

import os
import json
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout as auth_logout
from django.utils.timezone import now, localtime

from outsidemerch.decorators import render_to


# def logout(request):
#     """Logs out user"""
#     auth_logout(request)
#     return redirect('/')


JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lineup_2014_new.json'))
json_data=open(JSON_PATH)

lineups = json.load(json_data)
json_data.close()

STAGES = ["The Barbary", "Lands End", "Twin Peaks", "Sutro", "Panhandle", "The House by Heineken"]

def context(**extra):
    return dict(**extra)


@render_to('outsidemerch/overall.html')
def root(request, current_time=None):
    """Home view"""
    today = "2014-08-08"
    current = int(localtime(now()).strftime('%H%M')) if not current_time else int(current_time)
    stages = dict((k, []) for k in STAGES)
    for lineup in lineups:
        for show in lineup["shows"]:
            if show["date"] == today and int(show["time_end"]) >= current:
                show["artist"] = lineup["artist"]
                show["link"] = lineup["link"]
                stages[show["stage"]].append(show)
                break

    for k,v in stages.iteritems():
        a = [int(lineup["time_start"]) for lineup in v]
        if not a:
            continue
        min_time_start = str(min(a))
        stages[k] = [lineup for lineup in v if (lineup["time_start"] == min_time_start)]

    return context(stages=STAGES, lineups=stages)


@render_to('outsidemerch/stages.html')
def stages(request):
    """Stage view"""
    return context(stages=STAGES, lineups=lineups)


@render_to('outsidemerch/stages.html')
def stage(request, stage_id, current_time=None):
    """Stage view"""
    today = "2014-08-08"
    current = int(localtime(now()).strftime('%H%M')) if not current_time else int(current_time)
    stage = STAGES[int(stage_id) - 1]
    result = []
    for lineup in lineups:
        for show in lineup["shows"]:
            if show["date"] == today and show["stage"] == stage:
                show["artist"] = lineup["artist"]
                show["link"] = lineup["link"]
                result.append(show)
                break

    result = result[::-1]
    #
    # for k,v in stages.iteritems():
    #     a = [int(lineup["time_start"]) for lineup in v]
    #     if not a:
    #         continue
    #     min_time_start = str(min(a))
    #     stages[k] = [lineup for lineup in v if (lineup["time_start"] == min_time_start)]

    return context(stages=STAGES, lineups=result)