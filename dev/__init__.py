from redbot.core import dev_commands
from redbot.core.bot import Red
from redbot.core.errors import CogLoadError

from .dev import Dev, monkey_streams, unmonkey_streams


def setup(bot: Red):
    if not bot._cli_flags.dev:
        raise CogLoadError("This cog requires the `--dev` CLI flag.")
    if getattr(bot.get_cog("Dev"), "sessions", None):
        raise CogLoadError("End your REPL session(s) first.")
    bot.remove_cog("Dev")
    bot.add_cog(Dev())
    monkey_streams()


def teardown(bot: Red):
    unmonkey_streams()
    bot.remove_cog("Dev")
    bot.add_cog(dev_commands.Dev())
