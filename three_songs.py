import sys

class songs_selection_algo:
    '''
    music: List(int)
    opening_act_length: positive integer

    returns- boolean
    '''
    def get_best_three_songs(self, music, opening_act_length):
        # Todo: handle edge cases
        music.sort()

        # Since we dont want to iterate over last two tracks use '-2'  
        for index in range(len(music)-2):
            target = opening_act_length - music[index]

            # if sum of any two song is equal to target return True 
            if self.get_two_songs(music[index+1:], target):
                print(True)
                return True
            else:
                continue
        print(False)
        return False

    '''
    music: List(int)
    taget: positive integer

    returns- boolean
    '''
    def get_two_songs(self, music, target):
        analyzed = {}

        # Iterate though each songs and check if target-song_length exist in dict
        # If not add it to dict, else we found our two numbers
        for index, song_length in enumerate(music):
            remaining = target - song_length

            if remaining in analyzed:
                return True
            else:
                analyzed[song_length] = index
        return False

if __name__ == '__main__':
    test = songs_selection_algo()

    # Parse argumetns and convert to int
    if not sys.argv or len(sys.argv[1].split(','))<3:
        print "Error: Artist music should contain atleast three songs" 
        sys.exit() 
    music = [int(i) for i in sys.argv[1].split(',')]
    target = int(sys.argv[2])

    # call main function
    test.get_best_three_songs(music, target)