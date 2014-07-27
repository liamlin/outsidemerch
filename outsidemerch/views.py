# coding=utf-8

import os
import json
from django.utils.timezone import now, localtime

from outsidemerch.decorators import render_to


JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'lineup_2014_new.json'))
json_data=open(JSON_PATH)

lineups = json.load(json_data)
json_data.close()

STAGES = ["The Barbary", "Lands End", "Twin Peaks", "Sutro", "Panhandle", "The House by Heineken"]


def context(**extra):
    return dict(**extra)


@render_to('outsidemerch/overall.html')
def root(request, stage_id=None, current_time=None):
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

    stage = STAGES[int(stage_id) - 1] if stage_id else None
    return context(stages=STAGES, lineups=stages, specified_stage=stage)


def demo_time(request, current_time=None):
    return root(request, stage_id=None, current_time=current_time)


def demo_stage(request, stage_id=None):
    return root(request, stage_id=stage_id, current_time=None)


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
                if ((int(show["time_start"]) <= current <= int(show["time_end"])) or
                        (int(show["time_start"]) >= current and (int(show["time_start"]) - current) < 100)):
                    show["current"] = True
                else:
                    show["current"] = False
                result.append(show)
                break

    result = result[::-1]

    return context(stages=STAGES, lineups=result)