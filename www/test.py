#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import orm
from models import User
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    # u = User(name='Test', email='email@example.com', passwd='0123456789', image='about:blank')
    #
    # await u.save()

    u = User(name='Administrator', email='damin@example.com', passwd='233333333', image='about:blank')

    await u.save()

    u = User(name='Michael', email='michael@example.com', passwd='233333333', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
print('Compete !')
loop.close()