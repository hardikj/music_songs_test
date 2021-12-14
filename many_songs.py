import sys

# global matrix
matrix = [[-1 for i in range(100)] for j in range(100)]

class songs_selection_algo:
 
	def get_best_songs(self, music, n, total_time):
	     
	    # If the total_time is zero it means
	    # we got our expected total_time
	    if (total_time == 0):
	        return 1
	     
	    if (n <= 0):
	        return 0
	         
	    # If the value is not -1 it means it we already memorized the function
	    # hence save us some calls
	    if (matrix[n - 1][total_time] != -1):
	        return matrix[n - 1][total_time]
	         
	    # value of music[n-1] is greater than the total_time.
	    # lets call next value
	    if (music[n - 1] > total_time):
	        matrix[n - 1][total_time] = self.get_best_songs(music, n - 1, total_time)
	        return matrix[n - 1][total_time]
	    else:
	        matrix[n - 1][total_time] = self.get_best_songs(music, n - 1, total_time)
	        return matrix[n - 1][total_time] or self.get_best_songs(music, n - 1, total_time - music[n - 1])

if __name__ == '__main__':
    test = songs_selection_algo()

    # Parse argumetns and convert to int
    if not sys.argv or len(sys.argv[1].split(','))<3:
        print "Error: Artist music should contain atleast three songs" 
        sys.exit()
    music = [int(i) for i in sys.argv[1].split(',')]
    target = int(sys.argv[2])

    # call main function
    res = test.get_best_songs(music, len(music), target)
    if (res):
    	print "True"
    else:
    	print "False"
