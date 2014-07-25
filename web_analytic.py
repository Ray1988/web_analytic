__author__ = 'Lucky'


from datetime import datetime, timedelta
import sys

from bitmapist import setup_redis, delete_all_events, mark_event,\
                      MonthEvents, WeekEvents, DayEvents, HourEvents,\
                      BitOpAnd, BitOpOr


class Counter:

    def __init__(self):
        self.story_dict=dict()

        self.top_story_name_month=None
        self.top_story_count_month=-sys.maxint-1

        self.top_story_name_week=None
        self.top_story_count_week=-sys.maxint-1

        self.top_story_name_day=None
        self.top_story_count_day=-sys.maxint-1

        self.top_story_name_hour=None
        self.top_story_count_hour=-sys.maxint-1



    def mark_event(self, event_name, uuid, system='default', now=None, track_hourly=None):
        """
        """
        if event_name not in self.story_dict:
            self.story_dict[event_name]=True

        # mark event in bitmapist
        mark_event(event_name, uuid, system=system, now=now, track_hourly=track_hourly)

        # update most popular event
        self.update_most_popular_event(event_name,system)

    def update_most_popular_event(self,event_name,  system='default'):
        now=datetime.utcnow()

        if self.story_dict:
            if  event_name in self.story_dict.keys():
                month_count=len(MonthEvents(event_name, now.year, now.month, system=system))
                if month_count>self.top_story_count_month:
                    self.top_story_name_month=event_name
                    self.top_story_count_month=month_count

                week_count=len(WeekEvents(event_name, now.year, now.isocalendar()[1], system=system))
                if week_count>self.top_story_count_week:
                    self.top_story_name_week=event_name
                    self.top_story_count_week=week_count

                day_count=len(DayEvents(event_name, now.year, now.month, now.day, system=system))
                if day_count>self.top_story_count_day:
                    self.top_story_count_day=day_count
                    self.top_story_name_day=event_name

                hour_count=len(HourEvents(event_name, now.year, now.month, now.day, now.hour, system=system))
                if hour_count>self.top_story_count_hour:
                    self.top_story_count_hour=hour_count
                    self.top_story_name_hour=event_name

    def get_top_story(self, period):
        if period !='month' or 'week' or 'day' or 'hour':
            raise RuntimeError( "period should be month, week, day, or hour")
        option={'month':self.get_top_story_in_month,
                'week':self.get_top_story_in_week,
                'day':self.get_top_story_in_day,
                'hour':self.get_top_story_in_hour}

        return option[period]()

    def get_top_story_in_month(self):
        return {self.top_story_name_month:self.top_story_count_month}

    def get_top_story_in_week(self):
        return {self.top_story_name_week:self.top_story_count_week}

    def get_top_story_in_day(self):
        return {self.top_story_name_day:self.top_story_count_day}

    def get_top_story_in_hour(self):
        return {self.top_story_name_hour:self.top_story_count_hour}


"""
usage example

"""
c=Counter()
print "start"
print c.mark_event("firstevent", '123')
print c.mark_event("firstevent","121321")
print c.get_top_story_in_day()

