import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Function to play an MP3 file
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to stop playback
def stop_music():
    pygame.mixer.music.stop()

# Function to create a playlist
def create_playlist():
    playlist = []
    while True:
        print("\nPlaylist Management")
        print("Options:")
        print("1. Add a song to the playlist")
        print("2. Play the playlist")
        print("3. Stop the playlist")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            song_path = input("Enter the path of the MP3 file: ")
            if os.path.exists(song_path):
                playlist.append(song_path)
                print("Song added to the playlist.")
            else:
                print("File not found.")
        elif choice == '2':
            if not playlist:
                print("The playlist is empty.")
            else:
                for song in playlist:
                    play_music(song)
                    input("Press Enter to play the next song...")
                    stop_music()
        elif choice == '3':
            stop_music()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    create_playlist()
