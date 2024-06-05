from nextcord import Interaction, User, user_command
from nextcord.ext.commands import Cog

import config as _config
from bot import Bot


class UserCommand(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @user_command(name="name", force_global=True)
    async def ping(self, interaction: Interaction, target: User):

        await interaction.send(f"this is {target.name}")


def setup(bot: Bot):
    bot.add_cog(UserCommand(bot))
