import discord
from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    async def kick_command(self, ctx, member: discord.Member, reason=None):
        await member.kick(reason=reason)
        if reason is not None:
            await ctx.send(f'{member}, has been kicked from the server. Reason: {reason}')
        else:
            await ctx.send(f'{member}, has been kicked from the server.')

    @commands.command(name='ban')
    async def ban_command(self, ctx, member:discord.Member, reason=None):
        await member.ban(reason=reason)
        if reason is not None:
            await ctx.send(f'{member}, has been banned from the server. Reason: {reason}')
        else:
            await ctx.send(f'{member}, has been banned from the server.')

    @commands.command(name='clear')
    async def clear_command(self, ctx, amount: int):
        await ctx.send('Clearing messages.. this may take some time.')
        deleted = await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'Deleted {len(deleted)} messages')


def setup(bot):
    bot.add_cog(AdminCommands(bot))

