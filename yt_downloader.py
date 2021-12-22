from pytube import YouTube

link = input("Enter the link: ") # ask user for yt video to download
yt = YouTube(link) # pass user's link to YouTube class
stream = yt.streams.first()
stream.download() # this will download in your current working Dir
# Reveal info about the video
# Title
print("Title: ", yt.title)
# No. of views
print("Number of views: ", yt.views)
# Length of video
print("Length of video: ", yt.length,"seconds")
# Description of video
print("Description: ", yt.description)
# Rating
print("Ratings: ", yt.rating)
