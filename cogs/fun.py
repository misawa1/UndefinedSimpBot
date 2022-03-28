import discord

from discord.ext import commands

import wikipedia, asyncio, random, time, datetime

from aiohttp import ClientSession

start_time = time.time()



class Fun(commands.Cog):

	def __init__(self, bot):

		self.bot = bot


	# wiki search command here

	@commands.command(aliases = ['wsearch'])
	async def wiki(self, ctx, *, question):

		try:

			embed = discord.Embed( color = 0x07C9F5, timestamp = ctx.message.created_at)

			embed.add_field(
				name = "Searched-", 
				value = f"`{wikipedia.summary(question, sentences = 2)}`", 
				inline = True
				)

			await ctx.send(embed = embed)

		except:

			embed = discord.Embed(title = ' Invalid Command ', color = 0x07C9F5)
			await ctx.send(embed = embed)

	@commands.command(aliases = ['8b'])
	async def eightball(self, ctx, question: Option(str)):

		ballResponses = [

		"Yes", 'No', 'Take a wild guess...', 'Very doubtful', 'Sure',
		'Without a doubt', 'Most likely', 'Might be possible', 'Might not possible',
		'You will be judge', 'No...', 'No...B-baka!', 'i think...', 'I-\ndont know what to say', 'gg'

		]

		answer = random.choice(ballResponses)
		await ctx.respond(f"**Question: ** {question}\n**Answer:** {answer}")


    
    

def setup(bot):
	bot.add_cog(Fun(bot))
