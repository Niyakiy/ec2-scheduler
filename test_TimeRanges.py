#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import TimeRanges


class TimeRangesTestCase(unittest.TestCase):
    """ tests for TimeRanges class """

    def setUp(self):
        self.simple_valid_range = "00:00-23:59"
        self.invalid_range = "00:00-24:59"
        self.long_timeranges = "21:50-23:25,9:00-11:00,6:00-8:00,0:00-7:00,2:00-4:00,6:00-7:00," \
                "6:30-7:00,14:00-20:00,19:00-22:00,23:15-23:30"

    def test_parsing_invalid(self):
        """does "0:00-24:59" range not parsed"""
        self.assertFalse(TimeRanges.TimeRanges(self.invalid_range).is_valid)

    def test_parsing_simple(self):
        """does "00:00-23:59" timeranges parsed correctly"""
        self.assertTrue(TimeRanges.TimeRanges(self.simple_valid_range).is_valid)

    def test_parsing_extended(self):
        """does large overlapping timerange values parsed correctly"""
        self.assertTrue(TimeRanges.TimeRanges(self.long_timeranges).is_valid)

    def test_merge_simple(self):
        """does "00:00-23:59" ranges merged properly"""

        tr = TimeRanges.TimeRanges(self.simple_valid_range)
        self.assertEqual(tr.merged_ranges, [[0, 1439]])

    def test_merge_extended(self):
        """does large timerange ranges merged properly"""
        tr = TimeRanges.TimeRanges(self.long_timeranges)
        self.assertEqual(tr.merged_ranges, [[0, 480], [540, 660], [840, 1410]])

if __name__ == '__main__':
    unittest.main()
