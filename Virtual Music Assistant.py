import random

decades = ['80s', '90s', '2000s']
genres = ['Pop', 'Rock', 'Country']

artists = {
    '80s': {
        'Pop': ['Whitney Houston', 'Wham!', 'Rick'],
        'Rock': ['John Lennon', 'Bon Jovi', 'Metallica'],
        'Country': ['The Judds', 'Alabama', 'Dolly Parton']
    },
    '90s': {
        'Pop': ['Backstreet Boys', 'Mariah Carey', 'Spice Girls'],
        'Rock': ['Nirvana', 'Radiohead', 'Snoop Dog'],
        'Country': ['Shania Twain', 'Sawyer Brown', 'The Chicks']
    },
    '2000s': {
        'Pop': ['Taylor Swift', 'Ed Sheeran', 'Rihanna'],
        'Rock': ['Linkin Park', 'Arctic Monkeys', 'Blink 182'],
        'Country': ['Joseph Vincent', 'Josh Turner', 'Carrie Underwood']
    }
}

song_choice = {
    'Whitney Houston': 'I Wanna Dance with Somebody', 
    'Wham!': 'Last Christmas', 
    'Rick': 'Never Gonna Give You Up', 
    'John Lennon': 'Imagine', 
    'Bon Jovi': 'You Give Love a Bad Name', 
    'Metallica': 'Nothing else matters',
    'The Judds': 'Why Not Me', 
    'Alabama': 'Song of the South', 
    'Dolly Parton': 'Jolene',
    'Backstreet Boys': 'I want it that way', 
    'Mariah Carey': 'All I Want from Christmas is You', 
    'Spice Girls': 'Wannabe', 
    'Nirvana': 'Smells like Teen Spirit', 
    'Radiohead': 'Creep', 
    'Snoop Dog': 'Young, Wild & Free',
    'Shania Twain': 'Man! I feel like a Woman', 
    'Sawyer Brown': 'Some Girls Do' , 
    'The Chicks': 'Cowboy take me away',
    'Taylor Swift': 'Bad Blood', 
    'Ed Sheeran': 'Shape Of You', 
    'Rihanna': 'Umbrella',
    'Linkin Park': 'In the End', 
    'Arctic Monkeys': 'I Wanna Be Yours', 
    'Blink 182': 'All the Small Things',
    'Joseph Vincent': 'Can\'t take my eyes off you', 
    'Josh Turner': 'Your Man', 
    'Carrie Underwood': 'Before He Cheats'
}

fun_fact = {
    'Whitney Houston': 'Whitney Houston began singing in church as a child.',
    'Wham!': 'They were one of the most successful pop acts during the 1980s',
    'Rick': 'Astley himself has been rickrolled a few times; in fact, the first time he was rickrolled actually pre-dated the viral phenomenon.',
    'John Lennon': 'Lennon didn\'t pass his driving test until he was 25. He didn\'t drive much even after that, most famously crashing his white Mini on a trip to Scotland in 1969.',
    'Bon Jovi': 'The band held a contest to find opening acts for each of the shows on its new tour.',
    'Metallica': 'Metallica set a Guinness World Record for becoming the first musical act to perform on every continent.',
    'The Judds': 'Their first single release, “Had a Dream (For the Heart)” (1983), made the Billboard Country Singles chart.',
    'Alabama': 'Alabama is the most awarded band in the history of country music, with over 200 awards from a variety of organizations.',
    'Dolly Parton': 'Dolly Parton worked as a work as an actor, a successful businesswoman, and a philanthropist.',
    'Backstreet Boys': 'The Backstreet Boys have sold over 100 million records worldwide, making them the best-selling boy band of all time, and one of the world\'s best-selling music artists.',
    'Mariah Carey': 'Carey takes after her mother, who is a Juilliard-trained opera singer and a vocal coach.',
    'Spice Girls': 'Spice Girls are the only British act and girl group in UK music history to have achieved 6 consecutive #1 singles in a row.',
    'Nirvana': 'In the “Smells Like Teen Spirit” music video, the janitor is a reference to Kurt Cobain\'s old job at his old high school.',
    'Radiohead': 'Radiohead\'s selling point is not their identification with any one genre but their way of ranging over music as a whole.',
    'Snoop Dog': 'Snoop Dog once quit rapping and changed his name to Snoop Lion.',
    'Shania Twain': 'Shania Twain started performing bars when she was only 8 years old!',
    'Sawyer Brown': 'They went on to win the $100,000 first prize in \'84 on “Star Search,” and soon landed a record deal.',
    'The Chicks': 'At the 2007 Grammy Awards, the Dixie Chicks received the top three honours—album of the year, song of the year, and record of the year—becoming the first all-female group to win in any of those categories.',
    'Taylor Swift': 'The pop superstar\'s latest release, "1989 (Taylor\'s Version)", sold 580,000 copies in vinyl during its first week, making it the fastest-selling vinyl record ever since the stat was first tracked in 1991.',
    'Ed Sheeran': 'He names his guitars! They\'re called Lloyd, Felix, Cyril and Nigel!',
    'Rihanna': 'She signed her first record deal at 16 years old.',
    'Linkin Park': 'The band became very famous with their first album, Hybrid Theory, which was given a diamond certification by the RIAA for selling more than 10 million copies.',
    'Arctic Monkeys': 'Arctic Monkeys were heralded as one of the first bands to come to public attention via the Internet.',
    'Blink 182': 'The number 182 was added much after the band was formed and it does not have any real meaning.',
    'Joseph Vincent': 'He is of Filipino descent. Vincent picked up his first guitar when he was 15 and started by playing song covers.',
    'Josh Turner': 'Growing up in the church, he founded a gospel quartet called Thankful Hearts.',
    'Carrie Underwood': 'She sang for church, school, and talent shows BUT she didn\'t always plan to sing as a career. She was studying Journalism in college.'
}

user_playlists = {}

# Function to generate a random song
def generate_random_song():
    random_decade = random.choice(decades)
    random_genre = random.choice(genres)
    artists_for_selection = artists[random_decade][random_genre]
    random_artist = random.choice(artists_for_selection)
    random_song = song_choice[random_artist]
    return random_artist, random_song

# Function to show all artists and their songs
def show_all_artists_and_songs():
    print("All Artists and Songs:")
    for decade, genre_list in artists.items():
        for genre, artists_list in genre_list.items():
            for artist in artists_list:
                song = song_choice[artist]
                print(f"{artist} ({decade}, {genre}): '{song}'")

# Function to create playlists     
def create_playlist():
    playlist_name = input("Enter the name for your new playlist: ")
    user_playlists[playlist_name] = []  

    while True:
        print("Choose an artist from the available options or type 'exit' to finish adding songs.")
        artists_for_selection = artists[year_song][genre_song]
        print()

        print('Please choose one of the following singers:')
        for singer in artists_for_selection:
            print(singer)

        artist_choice = input("Enter the artist you want to add to your playlist: ")

        if artist_choice == 'exit':
            break

        if artist_choice in song_choice:
            user_playlists[playlist_name].append((artist_choice, song_choice[artist_choice]))
            print(f"Added '{song_choice[artist_choice]}' by {artist_choice} to the playlist.")
            print()
        else:
            print("Invalid artist name. Please choose from the available options.")

# Function to display the playlist
def display_playlists():
    if not user_playlists:
        print("You don't have any playlists yet.")
    else:
        print("Your Playlists:")
        for playlist_name, songs in user_playlists.items():
            print(f"--- {playlist_name} ---")
            for artist, song in songs:
                print(f"{song} by {artist}")
            print()

# Main
print('==========================================')
print('Welcome to your personal Virtual Spoti-Fi')
print('------------------------------------------')

file_path = '/Users/simranshah/assignments/simranshah_a7.py'

with open(file_path, 'r') as file:
    line_count = 0
    char_count = 0
    for line in file:
        line_count += 1
        char_count += len(line)
        print(f"{line_count}: {line.rstrip()}")  #Print line number and its content

print ('==========================================')
print ('Line Count:', line_count)  #Display the line count
print ('Character Count:', char_count) #Display the character count


while True:
        print()
        print("What would you like to do?")
        print("1. Pick specific music")
        print("2. Get a random song")
        print("3. Show all artists and songs")
        print("4. Show your playlists")
        selection = input("Enter your choice (1/2/3/4): ")
        print()

        if selection == '1':
            while True:
                choice_one = input('Would you like to go ahead and pick out some songs based on your current vibe? (Y/N): ')
                if choice_one != 'Y':
                    break

                while choice_one == 'Y':
                    print()
                    year_song = input(f'Please choose one of these decades whose music you want to listen to: {decades} ')
                    print()
                    genre_song = input(f'Please choose one of these genres of music you want to listen to: {genres} ')
                    print()

                    artists_for_selection = artists[year_song][genre_song]

                    print('Please choose one of the following singers:')
                    for singer in artists_for_selection:
                        print(singer)

                    print()
                    singer = input('Enter the singer you want to listen to: ')
                    print()

                    print(f"You are now listening to '{song_choice[singer]}' by {singer}")
                    print(f"A fun fact about the singer: '{fun_fact[singer]}'")
                    print()

                    choice_playlist = input('Would you like to create a playlist? (Y/N): ')
                    if choice_playlist == 'Y':
                        create_playlist()

                    choice_one = input('Would you like to choose different music? (Y/N): ')
                    if choice_one == 'N':
                        display_choice = input('Would you like to see your playlists? (Y/N): ')
                        if display_choice == 'Y':
                            display_playlists()
                        else:
                            break
            

        elif selection == '2':
            random_artist, random_song = generate_random_song()
            print(f"You are now listening to '{random_song}' by {random_artist}")
            print(f"A fun fact about the singer: '{fun_fact[random_artist]}'")
            print()
            choice_playlist = input('Would you like to create a playlist? (Y/N): ')
            if choice_playlist == 'Y':
                create_playlist()

        elif selection == '3':
            show_all_artists_and_songs()

        elif selection == '4':
            display_playlists()

        choice_one = input('Would you like to choose different music or explore more? (Y/N): ')
        if choice_one == 'N':
            break

print('------------------------------------------')
print('THANK YOU FOR LISTENING. COME BACK SOON!')
print('==========================================')
