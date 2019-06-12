#!/usr/bin/python3
# -*- coding: utf-8 -*-
from manifest import *
import requests


response = requests.get(UI_HOST + '/container/deleteTable')
response = requests.get(UI_HOST + '/flow/deleteTable')
