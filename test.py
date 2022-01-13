from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/809088073937846292/5jo7i6Hdw3jvDIU_QGHJ8ly0p19NQNXTSznxs6R9f5qRiaTfYVe0eZEemFoTTE6yEt_D', username="New Webhook Username")

embed = DiscordEmbed(title='Embed Title', description='Your Embed Description', color='03b2f8')
embed.set_author(name='Author Name', url='https://github.com/lovvskillz', icon_url='https://www.freeiconspng.com/uploads/growth-icon-28.png')
embed.set_footer(text='Embed Footer Text')
embed.set_timestamp()
embed.add_embed_field(name='Field 1', value='Lorem ipsum', inline=False)
embed.add_embed_field(name='Field 2', value='dolor sit', inline=False)
embed.add_embed_field(name='Field 3', value='amet consetetur')
embed.add_embed_field(name='Field 4', value='sadipscing elitr')

webhook.add_embed(embed)
response = webhook.execute()