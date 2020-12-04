# discordbot

# Command Usages

# Command Prefix = $

# Command red:
# aliases = r, sub
# Grabs a random post from a designated subreddit, default is r/memes
# Optional Parameter is the name of the subreddit, no spaces or special characters
# Example
> $r wholesome
# returns a post from the r/wholesome subreddit

> $sub cursedimages
# returns a post from the r/cursedimages subreddit

# Command test:
# Send a test message to the text channel, optional paramter is a single word that
# will be repeated by the bot
# Example
> $test Hello
# returns "Hello"

$ Command weather:
# aliases = w
# Grabs the current weather report from Open Weather Maps,
# and sends it to the text channel. The default city is Toms River, NJ
# Optional Parameter is the city name:
# It can  be just a city name, or if in the US, a city name followed by a state code, seperated by a comma
# Example
> $weather New York City
> returns the current weather report for New York City, NY

> $w Beachwood, NJ
# returns the current weather report for Beachwood, NJ

# Command random:
# aliases = rand
# Generates a random integer between two numbers; by default 0 and 100
# Optional Parameters
# To change the range to generate a number for, enter the lower and upper bounds, seperated by spaces
# Example
> $rand
> returns a random integer between 0 and 100

> $random -100 1000
# returns a random integer between -100 and 1000 (You must enter both bounds)

# Command sarcasm:
# aliases = sar
# Makes a phrase look sarcastic by randomizing capitalization
# Parameter
# You must enter a phrase for the bot to use, try to refrain from using double quote marks,
# as it has a slim chance to break and send an error
# Example
> $sar Hello World!
# returns something similar to "hEllO wOrLD!"

# Command delete:
# aliases = purge
# mass deletes messages in a text channel
# By default it will delete 100 messages, but you can specify the number
> $purge
# deletes 100 messages

> $delete 10
# deletes 10 messages

# Command morse:
# aliases = m, morsecode
# Converts a phrase into morse code, and returns it to the channel
> $morse Hello World!
# returns the morse code for Hello World
