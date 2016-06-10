#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

RANGES_LIST_REGEX = "^(([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]-([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9],)*" \
                    "(([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]-([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9])$"


class TimeRanges:
    def __init__(self, raw_range_data):
        self.ranges = []
        self.merged_ranges = []
        self.raw_data = raw_range_data
        self.is_valid = self.validate_and_parse()

    def __repr__(self):
        return "TimeRanges: {}, \nMergedTimeRanges: {}".format(self.ranges, self.merged_ranges)

    def __hhmm2minutes(self, hhmm):
        return int(hhmm.split(':')[0]) * 60 + int(hhmm.split(':')[1])

    def validate_and_parse(self):

        """
        Function to parse, validate and megre time ranges
        :return:
        True in case of valid and merged ranges
        """

        def overlaps(a, b):
            return a[0] <= b[0] <= a[1]

        def contains(a, b):
            return min(a[0], b[0]) == a[0] and max(a[1], b[1]) == a[1]

        def merge(a, b):
            return [min(a[0], b[0]), max(a[1], b[1])]

        if re.match(RANGES_LIST_REGEX, self.raw_data) is None:
            return False

        self.ranges = sorted([[self.__hhmm2minutes(i) for i in rng.split('-')] for rng in self.raw_data.split(',')],
                             key=lambda x: x[0])

        # Validating and merging
        for rng in self.ranges:
            # check if stop hour is less than start
            if rng[1] <= rng[0]:
                return False

            merged = False
            for ind, mrng in enumerate(self.merged_ranges):
                if contains(mrng, rng):
                    merged = True
                    break
                if overlaps(mrng, rng):
                    self.merged_ranges[ind] = merge(mrng, rng)
                    merged = True
                    break

            if rng not in self.merged_ranges and not merged:
                self.merged_ranges.append(rng)

        return True
