"""
The MIT License (MIT)

Original work Copyright (c) 2015 Rapptz
Modified work Copyright 2015 Jose Francisco Taas

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import click

import discordt

@click.command('discordt')
def main():
    dtcontroller = discordt.DTController()

    # instantaneous message display
    # set to false if bot will be sending messages
    dtcontroller.local_message_display = True

    # if you need access to discord.py's Discord.Client
    client = dtcontroller.dtclient.discordClient

    # only on_message and
    # on_ready have implementations in dtclient
    @dtcontroller.dtclient.event
    @asyncio.coroutine
    def on_message(message):
        pass

    @dtcontroller.dtclient.event
    @asyncio.coroutine
    def on_ready():
        # printing message on output box
        dtcontroller.print_output('Hello world!')

    # if you need the rest of the events:
    # but do not use on on_message and on_ready
    # as they will just get overwritten
    @dtcontroller.dtclient.discordClient.event
    @asyncio.coroutine
    def on_disconnect():
        pass

    # dtcontroller.run() -- just starts interface, must use /login
    # dtcontroller.run(email, password) -- logs in directly (bot use)
    dtcontroller.run()
