import utils


class CommandSender:

    @staticmethod
    def append_command(subcommand):
        utils.comm_to_send.append(subcommand)
        return utils.comm_to_send

    @staticmethod
    def command_to_send():
        return utils.comm_to_send
