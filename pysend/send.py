import os

import utils
#
# joiner = []
# joiner.append('ls')
# joiner.append('-l')
# comm = (" ".join(joiner))
# print(comm)
# send = os.popen(comm)
# out = send.read()
# print(out)

from utils.command_sender import CommandSender

CS = CommandSender()
CS.append_command('ls')
CS.append_command('-l')
print(CS.command_to_send())
