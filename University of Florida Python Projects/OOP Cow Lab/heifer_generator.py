from cow import Cow
from dragon import Dragon
from ice_dragon import IceDragon
from file_cow import FileCow
import os

class HeiferGenerator:

	cow_names = ['heifer', 'kitteh']

	quote_lines = '    \\\n' 
	quote_lines += '     \\\n'
	quote_lines += '      \\\n'

	cowImages = [	"        ^__^\n" +
					"        (oo)\\_______\n" +
					"        (__)\\       )\\/\\\n" +
					"            ||----w |\n" +
					"            ||     ||\n",


					"       (\"`-'  '-/\") .___..--' ' \"`-._\n" +
					"         ` *_ *  )    `-.   (      ) .`-.__. `)\n" +
					"         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n" +
					"      _.. `--'_..-_/   /--' _ .' ,4\n" +
					"   ( i l ),-''  ( l i),'  ( ( ! .-'\n"
	]

	dragon_names = ['dragon', 'ice-dragon']
	dragon_types = [Dragon, IceDragon]
	
	dragon_image =	"           |\\___/|       /\\  //|\\\\\n" + \
					"           /0  0  \\__   /  \\// | \\ \\\n" + \
					"          /     /  \\/_ /   //  |  \\  \\\n" + \
					"          \\_^_\\'/   \\/_   //   |   \\   \\\n" + \
					"          //_^_/     \\/_ //    |    \\    \\\n" + \
					"       ( //) |        \\ //     |     \\     \\\n" + \
					"     ( / /) _|_ /   )   //     |      \\     _\\\n" + \
					"   ( // /) '/,_ _ _/  ( ; -.   |    _ _\\.-~       .-~~~^-.\n" + \
					" (( / / )) ,-{        _      `.|.-~-.          .~         `.\n" + \
					"(( // / ))  '/\\      /                ~-. _.-~      .-~^-.  \\\n" + \
					"(( /// ))      `.   {            }                 /      \\  \\\n" + \
					" (( / ))     .----~-.\\        \\-'               .~         \\  `.   __\n" + \
					"            ///.----..>        \\            _ -~            `.  ^-`  \\\n" + \
					"              ///-._ _ _ _ _ _ _}^ - - - - ~                   `-----'\n"

	cows = None
	file_cows = None

	def get_cows():
		if HeiferGenerator.cows is None:
			HeiferGenerator.cows = [None]*(len(HeiferGenerator.cow_names) + len(HeiferGenerator.dragon_names))
			# add the 'regular' cows
			num_regular = len(HeiferGenerator.cow_names)
			for index in range(num_regular):
				HeiferGenerator.cows[index] = Cow(HeiferGenerator.cow_names[index])
				HeiferGenerator.cows[index].image = HeiferGenerator.quote_lines + HeiferGenerator.cowImages[index]
			
			# add the dragons
			for index in range(len(HeiferGenerator.dragon_names)):
				HeiferGenerator.cows[num_regular + index] = HeiferGenerator.dragon_types[index](
					HeiferGenerator.dragon_names[index],
					HeiferGenerator.quote_lines + HeiferGenerator.dragon_image
				)
			
		return HeiferGenerator.cows
	
	def filter(filename):
		return filename.endswith('.cow')

	def get_file_cows():
		if HeiferGenerator.file_cows is None:
			HeiferGenerator.file_cows = []
			for filename in os.listdir('./cows'):		
				if HeiferGenerator.filter(filename):
					c = FileCow(filename[0:-4], filename)
					HeiferGenerator.file_cows.append(c)

		return HeiferGenerator.file_cows
