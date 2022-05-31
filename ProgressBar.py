import random, time

BAR = chr(9608) #character 9608 is a blackbox

def main():
    # This will simulate the download
    print("Progress Bar simulation by Don")
    bytesDownloaded = 0
    downloadsize = 4096
    while bytesDownloaded < downloadsize:
        # lets try this with a random amount of progress
        bytesDownloaded += random.randint(0, 100)
         
        #lets now get the progress 
        barstr = getProgressBar(bytesDownloaded, downloadsize)
            
        print(barstr, end = "", flush= True)
            
        time.sleep(2) #It would pause for 2 secs
            #we now print back spaces to move the text cursor to the start line
        print("\b" * len(barstr), end="", flush= True) #The flush method will clear the internal buffer of the file
            
def getProgressBar(progress, total, barWidth = 40):
    """Returns a string that represents a progress bar that has a barwidth and total amount of progress"""
    
    progressBar = ""
    progressBar += "[" # This will create the left end of the progress bar
    
    #Make sure your progressBar is between 0 and total
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0
        
    #Calculating the num of bars to be displayed
    numberOfBar = int(progress / total) * barWidth
    
    progressBar += BAR * numberOfBar
    progressBar += "" * (barWidth - numberOfBar) #This will add the empty spaces
    progressBar += "]" #The right of the progressBAR
    
    #Cal the % complete
    percentageComplete = round(progress / total * 100, 1)
    progressBar += " " + str(percentageComplete) + "%"
    
    #Add the numbers
    progressBar += " " + str(progress) + "/" + str(total)
    
    return progressBar 

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    