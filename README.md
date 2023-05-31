# NFT Collection Stats Discord Bot

The following discord bot was specifically made for a certain NFT collection named Rubber Duck Bath Party, though, it can easily be adapted to other collection. It gives the lastest information for the set taken from Opensea (marketplace for NFTs). 

# General Information

* The main purpose of the bot is to showcase information for the Rubber Duck Bath Party (NFT set) from Opensea.
* The Information is shown through chat commands. 
* On the side bar the bot shows the current floor price as a watching activiy.

# Technologies

* The app uses Discord Developer Portal API to bring the bot alive.
* And for correct data it makes request to the opensea API.
* The programming language is python. No advanced skills used.

# Standard setup to run the bot: 

* Firstly, generate your own discord app. Don't know how? Here is a link for the discord devs portal documentation: https://discord.com/developers/docs/intro
* Now, get your own private key from the discord devs portal app and replace it in line 108 where it says client.run('{replace with key}')
* All that is left is to start the application.
* Now the bot should be online and listening for commands.

# List of supported commands:

Command Prefix: "."

* Daily: .daily volume; .daily sales; .daily average price
* Seven Day: .seven day volume; .seven day sales; .seven day average price
* Thirty Day: .thirty day volume; .thirty day sales; .thirty day average price
* Overall Stats: .total supply; .total volume; .total owners; .average price; .market cap

# How it looks like? Here is a screenshot:

![]()![discordBot](https://user-images.githubusercontent.com/102682394/235350199-81b0b4fd-c97b-4702-8965-89ed870ea84e.png)

# Other

If you want to use the bot for other NFT set you can do it by simply replacing the link for Rubber Duck Bath Party with link for other NFT collection.










