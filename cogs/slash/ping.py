from nextcord import Embed, Interaction, slash_command
from nextcord.ext.commands import Cog

import config as _config
from bot import Bot


class Ping(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @slash_command(description="Ping command", force_global=True)
    async def ping(self, interaction: Interaction):
        await interaction.send(f"Pong! {self.bot.latency * 1000:.2f}ms")


def setup(bot: Bot):
    bot.add_cog(Ping(bot))
