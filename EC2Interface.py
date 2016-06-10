#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3

class EC2Interface:

    def __init__(self):
        self.regions = []
        self.ec2_connection = None

    def connect(self):
        # trying to establish connection to AWS EC2
        try:
            self.ec2_connection = boto3.client('ec2')
        except Exception as e:
            print(e)

        if self.ec2_connection is not None:
            self.__load_ec2_regions()


    def __load_ec2_regions(self):
        for region in self.ec2_connection.describe_regions()['Regions']:
            self.regions.append(region['RegionName'])

    def __load_region_instances(self):
        for region in self.regions:
            filters = {'tag_key=EC2Sceduler'}


